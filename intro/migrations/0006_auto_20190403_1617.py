# Generated by Django 2.1.5 on 2019-04-03 10:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('intro', '0005_auto_20190403_1103'),
    ]

    operations = [
        migrations.RenameField(
            model_name='education',
            old_name='favourite',
            new_name='is_favourite',
        ),
    ]
