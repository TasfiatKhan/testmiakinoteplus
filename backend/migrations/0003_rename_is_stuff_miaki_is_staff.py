# Generated by Django 3.2.9 on 2021-11-26 20:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_auto_20211127_0213'),
    ]

    operations = [
        migrations.RenameField(
            model_name='miaki',
            old_name='is_stuff',
            new_name='is_staff',
        ),
    ]
