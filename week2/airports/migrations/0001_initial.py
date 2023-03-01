# Generated by Django 4.1.6 on 2023-02-24 15:41

from django.db import migrations, models

from airports.models import Airport


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('airport_code', models.CharField(max_length=3)),
                ('address', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=2)),
                ('zipcode', models.CharField(max_length=5)),
                ('is_open', models.BooleanField()),
            ],
        ),
    ]


class Runway(models.Model):
    LEFT = 'L'
    CENTER = 'C'
    RIGHT = 'R'
    NONE = 'N'
    RUNWAY_DESIGNATION_CHOICES = [
        (LEFT, 'Left'),
        (CENTER, 'Center'),
        (RIGHT, 'Right'),
        (NONE, 'None'),
    ]
    runway_number = models.IntegerField()
    runway_designation = models.CharField(
        max_length=1,
        choices=RUNWAY_DESIGNATION_CHOICES,
        default=NONE
    )
    length = models.IntegerField()
    width = models.IntegerField()
    airport = models.ForeignKey(Airport, on_delete=models.CASCADE)
