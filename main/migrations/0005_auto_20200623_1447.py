# Generated by Django 3.0.7 on 2020-06-23 14:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0004_auto_20200623_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='distributor',
            name='manufacturer',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='main.Manufacturer'),
        ),
        migrations.AlterField(
            model_name='distributor',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
