# Generated by Django 3.0.7 on 2020-07-09 15:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0002_auto_20200709_1526'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='uid',
            new_name='_uid',
        ),
    ]