# Generated by Django 4.2.5 on 2023-11-04 00:35

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("Kolekto", "0033_compra_nome_comprador"),
    ]

    operations = [
        migrations.RenameField(
            model_name="compra",
            old_name="trasportadora",
            new_name="transportadora",
        ),
    ]