# Generated by Django 3.2.3 on 2021-07-22 09:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pgapp', '0002_payment_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='order_id',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AddField(
            model_name='payment',
            name='time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='payment',
            name='payment_id',
            field=models.CharField(default='', max_length=300),
        ),
    ]