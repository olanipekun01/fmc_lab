# Generated by Django 2.2 on 2023-11-30 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Investigations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('investigation_name', models.CharField(max_length=500)),
                ('investigation_id', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Specimens',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specimen_name', models.CharField(max_length=500)),
                ('specimen_id', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Wards',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ward_name', models.CharField(max_length=500)),
                ('ward_id', models.CharField(max_length=200)),
            ],
        ),
    ]
