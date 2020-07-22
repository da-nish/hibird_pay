# Generated by Django 3.0.8 on 2020-07-22 14:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('userpay', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='current_plan',
            field=models.CharField(choices=[('Browse+ | 12MBPS', 'Browse+ | 12MBPS'), ('Pace+ | 20MBPS', 'Pace+ | 20MBPS'), ('Quick+ | 50MBPS', 'Quick+ | 50MBPS')], default=12, max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='plan_amount',
            field=models.PositiveIntegerField(),
        ),
        migrations.CreateModel(
            name='TransactionDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(max_length=50)),
                ('payment_id', models.CharField(max_length=50)),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('payment_month', models.CharField(choices=[('Jan', 'Jan'), ('Feb', 'Feb'), ('Mar', 'Mar'), ('Apr', 'Apr'), ('May', 'May'), ('Jun', 'Jun'), ('Jul', 'Jul'), ('Aug', 'Aug'), ('Sep', 'Sep'), ('Oct', 'Oct'), ('Nov', 'Nov'), ('Dec', 'Dec')], max_length=3)),
                ('success', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
