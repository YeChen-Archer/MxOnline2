# Generated by Django 2.2 on 2020-02-25 13:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0003_auto_20200222_2114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursecomments',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 25, 13, 5, 27, 304275), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='userask',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 25, 13, 5, 27, 304275), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='usercourse',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 25, 13, 5, 27, 304275), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='userfavorite',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 25, 13, 5, 27, 304275), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='usermessage',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 25, 13, 5, 27, 304275), verbose_name='添加时间'),
        ),
    ]
