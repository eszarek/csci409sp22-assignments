# Generated by Django 4.1.6 on 2023-03-13 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0003_tickets'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='num_people',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]