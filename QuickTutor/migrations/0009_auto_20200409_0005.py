# Generated by Django 3.0.2 on 2020-04-09 04:05

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('QuickTutor', '0008_auto_20200408_2353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='end_date_and_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 9, 5, 5, 51, 3727, tzinfo=utc)),
        ),
    ]
