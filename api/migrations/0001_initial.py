# Generated by Django 4.2.4 on 2023-08-08 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Book",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("author", models.CharField(max_length=100)),
                ("genre", models.CharField(max_length=20)),
                ("pub", models.CharField(max_length=100)),
                ("pub_date", models.DateTimeField(auto_now_add=True)),
                ("price", models.DecimalField(decimal_places=2, max_digits=5)),
            ],
            options={
                "ordering": ["title"],
            },
        ),
    ]
