# Generated by Django 2.1.2 on 2018-12-27 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Friends', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='friend',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]