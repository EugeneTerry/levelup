# Generated by Django 3.2.9 on 2021-12-14 05:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EventStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventstatus', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Gamer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.CharField(max_length=500)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GameType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gametype', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Games',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('game_creator', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='levelupapi.gamer')),
                ('gametype', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='levelupapi.gametype')),
            ],
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('attendees', models.ManyToManyField(related_name='MyEvents', to='levelupapi.Gamer')),
                ('creator', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='levelupapi.gamer')),
                ('eventstatus', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='levelupapi.eventstatus')),
                ('game', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='levelupapi.games')),
            ],
        ),
    ]
