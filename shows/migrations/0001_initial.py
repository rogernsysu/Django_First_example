# Generated by Django 4.1.3 on 2022-12-21 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Propagation_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Frequency', models.IntegerField()),
                ('Antenna_Height', models.DecimalField(decimal_places=0, max_digits=3)),
                ('EIRP', models.DecimalField(decimal_places=0, max_digits=3)),
            ],
        ),
    ]