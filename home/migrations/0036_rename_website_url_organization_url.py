# Generated by Django 3.2.4 on 2022-01-07 06:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0035_auto_20220107_0540'),
    ]

    operations = [
        migrations.RenameField(
            model_name='organization',
            old_name='website_url',
            new_name='url',
        ),
    ]
