# Generated by Django 3.0.7 on 2020-07-09 15:42

from django.db import migrations
import styleguide_example.common.fields


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0006_auto_20200709_1536'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='user_id',
            field=styleguide_example.common.fields.UidField(default='asd', max_length=28),
        ),
    ]
