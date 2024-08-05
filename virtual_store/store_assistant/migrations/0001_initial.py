# Generated by Django 5.0.3 on 2024-07-29 21:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.IntegerField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('location', models.CharField(max_length=255)),
                ('stock_availability', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerBehavior',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_id', models.IntegerField()),
                ('purchase_date', models.DateField()),
                ('purchase_amount', models.FloatField()),
                ('rating', models.IntegerField()),
                ('review', models.TextField()),
                ('search_queries', models.TextField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store_assistant.product')),
            ],
        ),
    ]
