# Generated by Django 5.1.1 on 2024-11-05 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Dataset",
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
                ("name", models.CharField(max_length=255)),
                ("description", models.TextField()),
                ("tags", models.CharField(max_length=255)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("is_public", models.BooleanField(default=True)),
                (
                    "dataset_type",
                    models.CharField(
                        choices=[
                            ("image", "Image"),
                            ("clinical", "Clinical Record"),
                            ("text", "Text Data"),
                            ("audio", "Audio Data"),
                            ("video", "Video Data"),
                            ("other", "Other Data"),
                        ],
                        max_length=50,
                    ),
                ),
                (
                    "license",
                    models.CharField(choices=[("mit", "MIT")], max_length=50),
                ),
                ("format", models.CharField(max_length=255)),
                ("file", models.FileField(upload_to="datasets/")),
                ("version", models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name="Rating",
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
                (
                    "rating",
                    models.IntegerField(
                        choices=[
                            (1, 1),
                            (2, 2),
                            (3, 3),
                            (4, 4),
                            (5, 5),
                        ]
                    ),
                ),
                ("review", models.TextField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
