# Generated by Django 5.0.4 on 2024-04-19 17:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fabrica_needs', '0002_rename_produtcs_produtc'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Produtc',
            new_name='Product',
        ),
    ]
