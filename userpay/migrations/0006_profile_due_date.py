# Generated by Django 3.0.8 on 2020-07-29 12:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userpay', '0005_plandetail_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='due_date',
            field=models.DateField(default=datetime.datetime(2020, 7, 29, 12, 2, 47, 112098)),
        ),
    ]