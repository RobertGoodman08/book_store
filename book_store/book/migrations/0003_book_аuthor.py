# Generated by Django 3.2.7 on 2021-09-14 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_auto_20210914_0802'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='аuthor',
            field=models.CharField(default=1, max_length=10000),
            preserve_default=False,
        ),
    ]
