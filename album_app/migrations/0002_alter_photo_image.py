# Generated by Django 4.1.5 on 2023-01-09 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("album_app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="photo",
            name="image",
            field=models.ImageField(upload_to=""),
        ),
    ]
