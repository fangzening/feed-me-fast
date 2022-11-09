# Generated by Django 3.1.2 on 2021-01-23 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0026_order_is_rated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('WAITING', 'WAITING'), ('CONFIRMED', 'CONFIRMED'), ('IN DELIVERY', 'IN DELIVERY'), ('DELIVERED', 'DELIVERED'), ('RATED', 'RATED')], max_length=20),
        ),
    ]
