# Generated by Django 3.0.7 on 2020-06-19 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='shop',
            name='email',
            field=models.EmailField(blank=True, max_length=255, null=True),
        ),
    ]
