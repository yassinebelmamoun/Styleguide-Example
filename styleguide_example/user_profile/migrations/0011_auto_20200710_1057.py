# Generated by Django 3.0.7 on 2020-07-10 10:57

from django.db import migrations
import styleguide_example.common.fields


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0010_auto_20200710_1040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user_id',
            field=styleguide_example.common.fields.UidField(default='E5iN8Z9ysPPJJxURLQkMGxkrukxS', max_length=28),
        ),
    ]
