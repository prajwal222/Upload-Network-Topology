# Generated by Django 3.1.3 on 2020-12-19 11:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Filename',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=100, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='YAMLEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(max_length=100, null=True)),
                ('host', models.CharField(blank=True, max_length=100, null=True)),
                ('username', models.CharField(blank=True, max_length=100, null=True)),
                ('password', models.CharField(blank=True, max_length=100, null=True)),
                ('device_type', models.CharField(blank=True, max_length=100, null=True)),
                ('filename', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='YAMLDatabase.filename')),
            ],
            options={
                'unique_together': {('filename', 'hostname')},
            },
        ),
    ]
