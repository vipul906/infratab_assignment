# Generated by Django 3.2.4 on 2021-06-05 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ratemymovie', '0002_auto_20210605_1535'),
    ]

    operations = [
        migrations.RenameField(
            model_name='people',
            old_name='movie_id',
            new_name='movie',
        ),
    ]
