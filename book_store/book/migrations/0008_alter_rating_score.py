# Generated by Django 3.2.7 on 2021-09-30 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0007_rating_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]