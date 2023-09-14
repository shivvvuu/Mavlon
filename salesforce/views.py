# views.py

from django.shortcuts import redirect
import requests
from django.http import HttpResponse
from project import settings
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import CustomUser
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login


def salesforce_login(request):
    authorization_url = f"https://login.salesforce.com/services/oauth2/authorize?response_type=code&client_id={settings.SALESFORCE_CLIENT_ID}&redirect_uri={settings.SALESFORCE_REDIRECT_URI}"
    return redirect(authorization_url)


def home(request):
    user =None
    code = request.GET.get('code')

    data = {
        'grant_type': 'authorization_code',
        'code': code,
        'client_id': settings.SALESFORCE_CLIENT_ID,
        'client_secret': settings.SALESFORCE_CLIENT_SECRET,
        'redirect_uri': settings.SALESFORCE_REDIRECT_URI,
    }
    response = requests.post('https://login.salesforce.com/services/oauth2/token', data=data)
    response_data = response.json()
    
    # Store the access token and perform further actions (e.g., user creation or login)
    if 'access_token' in response_data:
    
        # To check is User is exists or not in DB
        
        if user_exists(response_data['id']):
            print('===================LOGIN================')
            login(request, user)
            return redirect('/')
        else:
             # TO save the details provided by salesforce i.e Tokens, id, etc
            print("==============================SignUP======================")
            custom_user = CustomUser(
            access_token = str(response_data['access_token']),
            signature = response_data['signature'],
            instance_url = response_data['instance_url'],
            user_id = response_data['id'],
            token_type = response_data['token_type'],
            issued_at = response_data['issued_at']
            )
            custom_user.save()
            
            user = User.objects.create_user(
                username= response_data['id']
                )
            user.save()
            login(request, user)
            return redirect('/')
    else:
        return HttpResponse("OAuth token retrieval failed.", status=400)
    
def user_exists(username):
    return User.objects.filter(username=username).exists()
    
@login_required
def mavlon_page(request):
    return render(request, 'mavlon_page.html')

def login_page(request):
    return render(request, 'templates/login.html')
   