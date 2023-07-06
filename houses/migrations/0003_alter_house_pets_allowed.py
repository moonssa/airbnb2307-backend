# Generated by Django 4.2.3 on 2023-07-06 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0002_rename_price_house_price_per_night_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='pets_allowed',
            field=models.BooleanField(default=True, help_text='Does this house allow pets?'),
        ),
    ]