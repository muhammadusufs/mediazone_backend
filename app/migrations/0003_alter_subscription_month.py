# Generated by Django 4.2.4 on 2023-08-06 16:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_subscription_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='month',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 6, 16, 20, 10, 448422, tzinfo=datetime.timezone.utc)),
        ),
    ]
