# Generated by Django 5.0.1 on 2024-02-02 15:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ExchangeRate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_last_update', models.DateTimeField()),
                ('time_next_update', models.DateTimeField()),
                ('rate', models.FloatField()),
                ('currency_base', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_app.currency')),
                ('currency_final', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='currency_final', to='api_app.currency')),
            ],
            options={
                'ordering': ['-time_next_update'],
            },
        ),
    ]