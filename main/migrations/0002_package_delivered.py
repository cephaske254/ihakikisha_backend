# Generated by Django 3.0.7 on 2020-06-18 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='delivered',
            field=models.BooleanField(default=False),
        ),
    ]
