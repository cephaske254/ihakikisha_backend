# Generated by Django 3.0.7 on 2020-06-18 19:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0005_auto_20200618_1949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='distributor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='package',
            name='products',
            field=models.ManyToManyField(blank=True, to='main.Product'),
        ),
        migrations.AlterField(
            model_name='package',
            name='shop',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Shop'),
        ),
    ]
