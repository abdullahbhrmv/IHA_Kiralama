# Generated by Django 5.0.1 on 2024-03-11 12:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("ihaUygulamasi", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="iha",
            name="fotograf",
            field=models.ImageField(blank=True, null=True, upload_to="IHA_PHOTOS/"),
        ),
    ]