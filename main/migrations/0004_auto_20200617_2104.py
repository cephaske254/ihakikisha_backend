# Generated by Django 3.0.7 on 2020-06-17 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200617_2059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
