# Generated by Django 4.1.7 on 2023-03-20 13:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0007_remove_mycart_created_time'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MyCart',
        ),
    ]