# Generated by Django 4.1.6 on 2023-03-14 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0004_reservation_num_people'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='num_people',
            field=models.IntegerField(default=1),
        ),
    ]
