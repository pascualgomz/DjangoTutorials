# Generated by Django 5.0.2 on 2024-02-21 04:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pages", "0002_comment"),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="description",
            field=models.TextField(default="default"),
            preserve_default=False,
        ),
    ]
