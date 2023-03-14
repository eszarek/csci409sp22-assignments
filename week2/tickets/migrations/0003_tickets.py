# Generated by Django 4.1.6 on 2023-03-13 16:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0002_rename_tickets_reservation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tickets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seat', models.CharField(max_length=10)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('ticket_class', models.CharField(choices=[('F', 'F'), ('B', 'B'), ('M', 'M')], default='M', max_length=1)),
                ('reservation', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tickets.reservation')),
            ],
        ),
    ]
