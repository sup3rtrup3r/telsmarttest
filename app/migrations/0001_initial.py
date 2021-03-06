# Generated by Django 3.1.7 on 2021-03-16 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DeviceVendor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='DSS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.IntegerField()),
                ('value', models.CharField(max_length=255)),
                ('label', models.CharField(max_length=255)),
                ('dss_type', models.CharField(choices=[('blf', 'BLF'), ('spd', 'SPD')], default='spd', max_length=45, verbose_name='Dss type')),
            ],
        ),
        migrations.CreateModel(
            name='Extension',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('extension', models.IntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='DeviceModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('dss', models.BooleanField()),
                ('device_format', models.CharField(choices=[('pdf', 'PDF'), ('html', 'HTML'), ('xml', 'XML')], default='xml', max_length=255, verbose_name='Device format')),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.devicevendor')),
            ],
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('mac', models.CharField(max_length=255, unique=True)),
                ('cfg_last_update', models.DateTimeField(auto_now_add=True)),
                ('dss', models.ManyToManyField(to='app.DSS')),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.devicemodel')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.device')),
                ('extension', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.extension')),
            ],
        ),
    ]
