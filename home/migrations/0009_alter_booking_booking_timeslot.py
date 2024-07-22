# Generated by Django 4.2.14 on 2024-07-18 06:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_alter_booking_booking_timeslot_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='booking_timeslot',
            field=models.TimeField(choices=[(datetime.time(11, 0), '11:00 AM'), (datetime.time(12, 0), '12:00 PM'), (datetime.time(13, 0), '01:00 PM'), (datetime.time(14, 0), '02:00 PM'), (datetime.time(15, 0), '03:00 PM'), (datetime.time(19, 0), '07:00 PM'), (datetime.time(20, 0), '08:00 PM'), (datetime.time(21, 0), '09:00 PM'), (datetime.time(22, 0), '10:00 PM')], default=0),
        ),
    ]
