# Generated by Django 3.0.4 on 2020-04-09 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_slots'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slots',
            name='slot_date',
            field=models.DateField(),
        ),
    ]
