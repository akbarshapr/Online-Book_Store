# Generated by Django 4.1.7 on 2023-03-12 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('color', models.CharField(default='#000000', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.FloatField(blank=True, null=True)),
                ('image_url', models.CharField(blank=True, max_length=2083)),
                ('follow_author', models.CharField(blank=True, max_length=2083)),
                ('book_available', models.BooleanField()),
                ('genres', models.ManyToManyField(to='book.genre')),
            ],
        ),
    ]
