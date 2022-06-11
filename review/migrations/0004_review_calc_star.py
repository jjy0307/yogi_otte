# Generated by Django 4.0.5 on 2022-06-11 13:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0003_alter_review_create_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='calc_star',
            field=models.FloatField(null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
    ]