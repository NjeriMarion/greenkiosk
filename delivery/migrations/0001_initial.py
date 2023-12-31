# Generated by Django 4.2.2 on 2023-06-22 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Recipient_name', models.CharField(max_length=32)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('Delivery_item', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('date_requested', models.DateTimeField(auto_now_add=True)),
                ('no_of_products', models.PositiveIntegerField()),
                ('delivery_address', models.CharField(max_length=40)),
            ],
        ),
    ]
