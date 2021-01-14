# Generated by Django 3.1.5 on 2021-01-14 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CamApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('time', models.DateTimeField()),
                ('total_price', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'order',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='OrderList',
            fields=[
                ('list_id', models.AutoField(primary_key=True, serialize=False)),
                ('quatity', models.CharField(max_length=3)),
            ],
            options={
                'db_table': 'order_list',
                'managed': False,
            },
        ),
        migrations.AlterModelOptions(
            name='menu',
            options={'managed': False},
        ),
    ]
