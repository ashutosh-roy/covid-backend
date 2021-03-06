# Generated by Django 3.0.4 on 2020-04-09 09:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_shop'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slots',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slot_date', models.DateField(auto_now=True)),
                ('slot_time', models.TimeField()),
                ('user_id', models.CharField(max_length=10)),
                ('user_phno', models.CharField(max_length=10)),
                ('shopid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Shop')),
            ],
        ),
    ]
