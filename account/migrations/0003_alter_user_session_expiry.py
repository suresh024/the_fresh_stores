# Generated by Django 4.2.5 on 2023-09-17 08:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_user_session_expiry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='session_expiry',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 17, 8, 34, 54, 438477, tzinfo=datetime.timezone.utc)),
        ),
    ]
