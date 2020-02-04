# Generated by Django 3.0.3 on 2020-02-03 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Athlete',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('sex', models.CharField(blank=True, choices=[('M', 'M'), ('F', 'F')], default=None, max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField(blank=True, null=True)),
                ('height', models.IntegerField(blank=True, null=True)),
                ('weight', models.FloatField(blank=True, null=True)),
                ('year', models.IntegerField(blank=True, null=True)),
                ('games', models.CharField(max_length=100)),
                ('season', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('sport', models.CharField(max_length=100)),
                ('event', models.CharField(max_length=100)),
                ('medal', models.CharField(blank=True, max_length=20, null=True)),
                ('athlete_id', models.IntegerField()),
                ('noc', models.CharField(blank=True, max_length=3, null=True)),
                ('team', models.CharField(blank=True, max_length=60)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]