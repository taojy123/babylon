# Generated by Django 3.0.8 on 2020-08-04 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20200804_1141'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cache',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cookie', models.TextField(blank=True)),
                ('tk', models.TextField(blank=True)),
            ],
        ),
    ]