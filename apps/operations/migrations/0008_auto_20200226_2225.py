# Generated by Django 2.2 on 2020-02-26 22:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0007_auto_20200225_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursecomments',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 26, 22, 25, 16, 889144), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='userask',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 26, 22, 25, 16, 889144), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='usercourse',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 26, 22, 25, 16, 889144), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='userfavorite',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 26, 22, 25, 16, 889144), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='usermessage',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 26, 22, 25, 16, 889144), verbose_name='添加时间'),
        ),
    ]
