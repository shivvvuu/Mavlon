# Generated by Django 4.2.5 on 2023-09-14 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('access_token', models.CharField(max_length=1000)),
                ('signature', models.CharField(max_length=1000)),
                ('instance_url', models.CharField(max_length=1000)),
                ('user_id', models.CharField(max_length=1000, unique=True)),
                ('token_type', models.CharField(max_length=30)),
                ('issued_at', models.CharField(max_length=500)),
            ],
        ),
    ]
