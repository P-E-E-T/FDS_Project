# Generated by Django 4.2.5 on 2023-11-04 00:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Kolekto", "0034_rename_trasportadora_compra_transportadora"),
    ]

    operations = [
        migrations.AlterField(
            model_name="compra",
            name="data",
            field=models.DateField(auto_now_add=True),
        ),
    ]