# Generated by Django 3.0.8 on 2020-08-23 18:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userpay', '0011_transactiondetail_amount'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='user',
            new_name='userid',
        ),
    ]
