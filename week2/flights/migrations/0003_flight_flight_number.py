# Generated by Django 4.1.6 on 2023-03-13 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0002_airline_flight_airline'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='flight_number',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
