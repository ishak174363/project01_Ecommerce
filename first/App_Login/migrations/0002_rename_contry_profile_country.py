# Generated by Django 4.2.7 on 2023-11-24 09:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App_Login', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='contry',
            new_name='country',
        ),
    ]
