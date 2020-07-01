# Generated by Django 3.0.7 on 2020-07-01 13:24

from django.db import migrations, models
import main.validators


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200701_0931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='expires',
            field=models.DateField(blank=True, validators=[main.validators.validate_expires]),
        ),
    ]
