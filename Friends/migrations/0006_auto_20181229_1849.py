# Generated by Django 2.1.2 on 2018-12-29 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Friends', '0005_auto_20181229_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friend',
            name='birthday',
            field=models.TextField(),
        ),
    ]