# Generated by Django 4.2.4 on 2023-08-13 20:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="author",
            options={"ordering": ["id"]},
        ),
        migrations.AlterModelOptions(
            name="genre",
            options={"ordering": ["id"]},
        ),
        migrations.AlterModelOptions(
            name="publisher",
            options={"ordering": ["id"]},
        ),
    ]
