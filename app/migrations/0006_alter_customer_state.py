# Generated by Django 5.1.3 on 2024-12-10 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_product_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='state',
            field=models.CharField(max_length=200),
        ),
    ]