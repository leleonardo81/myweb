# Generated by Django 2.1.2 on 2018-12-29 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Friends', '0007_auto_20181229_1852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friend',
            name='gender',
            field=models.TextField(choices=[('Male', 'Male'), ('Female', 'Female')]),
        ),
    ]
