# Generated by Django 4.0.5 on 2022-06-08 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_reviews', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='title',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
