# Generated by Django 2.2 on 2020-02-22 21:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0002_auto_20200222_2055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursecomments',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 22, 21, 14, 41, 442430)),
        ),
        migrations.AlterField(
            model_name='userask',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 22, 21, 14, 41, 442430)),
        ),
        migrations.AlterField(
            model_name='usercourse',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 22, 21, 14, 41, 442430)),
        ),
        migrations.AlterField(
            model_name='userfavorite',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 22, 21, 14, 41, 442430)),
        ),
        migrations.AlterField(
            model_name='usermessage',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 22, 21, 14, 41, 442430)),
        ),
    ]
