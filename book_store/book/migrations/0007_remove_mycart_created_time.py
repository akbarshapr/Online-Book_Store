# Generated by Django 4.1.7 on 2023-03-20 05:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0006_remove_mycart_book_mycart_book'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mycart',
            name='created_time',
        ),
    ]
