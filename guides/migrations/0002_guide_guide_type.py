# Generated by Django 4.2.5 on 2023-09-23 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guides', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='guide',
            name='guide_type',
            field=models.CharField(blank=True, choices=[('бизнес', 'бизнес'), ('медицина', 'медицина'), ('образование', 'образование'), ('экология', 'экология'), ('суды', 'суды'), ('религия', 'религия')], max_length=100),
        ),
    ]
