# Generated by Django 3.0.7 on 2020-06-30 06:33

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import main.validators
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Farmer',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='profile_m', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('image', cloudinary.models.CloudinaryField(default='avatar.png', max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='profile', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=13, validators=[main.validators.validate_phone])),
                ('location', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('logo', cloudinary.models.CloudinaryField(default='avatar.png', max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProductSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('composition', models.TextField()),
                ('image', cloudinary.models.CloudinaryField(max_length=255)),
                ('date', models.DateField(auto_now_add=True)),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Manufacturer')),
            ],
            options={
                'unique_together': {('name',)},
            },
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('phone', models.IntegerField(unique=True)),
                ('location', models.CharField(max_length=255)),
                ('email', models.EmailField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'unique_together': {('name', 'phone', 'location'), ('name', 'location')},
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveIntegerField()),
                ('comment', models.TextField(blank=True, null=True)),
                ('product_set', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.ProductSet')),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('qr_code', cloudinary.models.CloudinaryField(blank=True, max_length=255)),
                ('sold', models.BooleanField(default=False)),
                ('manufactured', models.DateField(validators=[main.validators.validate_manufactured])),
                ('date', models.DateField(auto_now_add=True)),
                ('product_set', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='main.ProductSet')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('delivered', models.BooleanField(default=False)),
                ('date', models.DateField(auto_now_add=True)),
                ('distributor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('products', models.ManyToManyField(blank=True, to='main.Product')),
                ('shop', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Shop')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Distributor',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('user', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('manufacturer', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='main.Manufacturer')),
            ],
            options={
                'unique_together': {('user', 'manufacturer')},
            },
        ),
    ]
