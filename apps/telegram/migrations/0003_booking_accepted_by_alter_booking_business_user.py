# Generated by Django 5.0.6 on 2024-06-25 15:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telegram', '0002_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='accepted_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='telegram.userbusiness', verbose_name='Принято пользователем'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='business_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings_as_business_user', to='telegram.userbusiness', verbose_name='Бизнес пользователь'),
        ),
    ]
