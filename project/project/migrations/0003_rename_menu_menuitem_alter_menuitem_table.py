# Generated by Django 4.1.5 on 2023-01-21 18:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_menu_cuisine'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Menu',
            new_name='MenuItem',
        ),
        migrations.AlterModelTable(
            name='menuitem',
            table='MenuItem',
        ),
    ]
