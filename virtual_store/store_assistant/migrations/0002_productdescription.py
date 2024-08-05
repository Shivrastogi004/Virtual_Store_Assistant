# Generated by Django 5.0.3 on 2024-07-29 21:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_assistant', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductDescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='store_assistant.product')),
            ],
        ),
    ]
