# Generated by Django 2.1.2 on 2018-12-29 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Friends', '0003_auto_20181228_2141'),
    ]

    operations = [
        migrations.AddField(
            model_name='friend',
            name='gender',
            field=models.TextField(default=''),
        ),
    ]