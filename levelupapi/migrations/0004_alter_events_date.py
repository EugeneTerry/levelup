# Generated by Django 3.2.9 on 2022-01-08 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('levelupapi', '0003_events_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='date',
            field=models.DateTimeField(),
        ),
    ]