# Generated by Django 2.2 on 2019-04-12 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intro', '0007_auto_20190411_1633'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='image',
            field=models.CharField(default='https://images.pexels.com/photos/1010519/pexels-photo-1010519.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500', max_length=100),
            preserve_default=False,
        ),
    ]
