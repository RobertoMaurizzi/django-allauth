# Generated by Django 2.0.1 on 2018-01-23 09:30

from django.conf import settings
from django.db import migrations
from allauth.account import app_settings as account_settings

class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('socialaccount', '0003_extra_data_default_dict'),
    ]

    # this will be an empty migration unless ACCOUNT_USE_SITES is set
    # This might be a very bad idea however. I'm unsure what's the
    # best way to deal with settings-dependent schema change (even if
    # this change would not stop a Site-less installation from working,
    # there might be some undetected data corruption).
    # For sure if you don't USE_SITES it won't change your db... and
    # changing this "later" is extremely unlikely.
    # I hope to hear back from the original allauth author(s)
    if account_settings.USE_SITES:
        operations = [
            migrations.AlterUniqueTogether(
                name='socialaccount',
                unique_together={('user', 'provider', 'uid')},
            ),
        ]
    else:
        operations = [ ]


