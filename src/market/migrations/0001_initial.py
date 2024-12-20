# Generated by Django 5.1.3 on 2024-11-16 17:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('commodities', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MarketCommodity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity_kg', models.IntegerField(default=0)),
                ('expected_price_per_kg', models.DecimalField(decimal_places=2, max_digits=10)),
                ('expiry_date', models.DateField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('commodity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='market_commodities', to='commodities.commodity')),
            ],
        ),
    ]
