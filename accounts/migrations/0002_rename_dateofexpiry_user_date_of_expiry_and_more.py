# Generated by Django 4.2.5 on 2023-09-23 10:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='dateOfExpiry',
            new_name='date_of_expiry',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='dateOfIssue',
            new_name='date_of_issue',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='personalNumber',
            new_name='personal_number',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='placeOfBirth',
            new_name='place_of_birth',
        ),
    ]
