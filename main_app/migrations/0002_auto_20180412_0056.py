# Generated by Django 2.0.3 on 2018-04-12 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='money',
            name='cash',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='money',
            name='day_wage',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]
