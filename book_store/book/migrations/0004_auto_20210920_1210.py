# Generated by Django 3.2.7 on 2021-09-20 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_book_аuthor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='number_pages',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='book',
            name='аuthor',
            field=models.CharField(blank=True, max_length=10000),
        ),
    ]