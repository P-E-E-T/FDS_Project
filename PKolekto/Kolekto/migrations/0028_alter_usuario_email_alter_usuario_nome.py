# Generated by Django 4.2.6 on 2023-10-31 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Kolekto', '0027_denuncia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='email',
            field=models.EmailField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='nome',
            field=models.CharField(max_length=20, null=True),
        ),
    ]