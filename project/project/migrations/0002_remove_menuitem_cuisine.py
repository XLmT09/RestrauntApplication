# Generated by Django 4.1.5 on 2023-02-08 17:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menuitem',
            name='cuisine',
        ),
    ]