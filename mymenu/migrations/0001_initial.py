# Generated by Django 3.1.5 on 2021-05-02 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('menu_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30, unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='image')),
                ('des', models.TextField()),
                ('price', models.CharField(max_length=15)),
                ('cat', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'menu',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('total_price', models.IntegerField()),
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
                ('quantity', models.IntegerField(max_length=3)),
                ('price', models.IntegerField(max_length=3)),
                ('cup', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'order_list',
                'managed': False,
            },
        ),
    ]
