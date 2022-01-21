# Generated by Django 3.2.4 on 2022-01-21 18:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0056_merge_0055_auto_20220121_0505_0055_auto_20220121_0654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(error_messages={'required': 'You must enter a username', 'unique': 'A user with that username already exists.'}, help_text='Once a username is set, it cannot be changed.', max_length=22, unique=True, validators=[django.core.validators.RegexValidator('^[\\w\\d]+$', 'Username can only contain alphanumeric characters'), django.core.validators.MaxLengthValidator(22, 'Username must be less than 20 characters'), django.core.validators.MinLengthValidator(2, 'Username must be at least 2 characters')]),
        ),
    ]
