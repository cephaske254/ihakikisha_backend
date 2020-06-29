# Generated by Django 3.0.7 on 2020-06-25 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmer',
            name='image',
            field=models.URLField(default='avatar.png'),
        ),
        migrations.AlterField(
            model_name='manufacturer',
            name='logo',
            field=models.URLField(default='avatar.png'),
        ),
        migrations.AlterField(
            model_name='productset',
            name='image',
            field=models.URLField(),
        ),
    ]