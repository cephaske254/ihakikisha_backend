# Generated by Django 3.0.7 on 2020-06-25 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200625_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmer',
            name='image',
            field=models.ImageField(default='avatar.png', upload_to='profiles/farmer'),
        ),
        migrations.AlterField(
            model_name='manufacturer',
            name='logo',
            field=models.ImageField(default='avatar.png', upload_to='profiles/manufacturer'),
        ),
        migrations.AlterField(
            model_name='productset',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]