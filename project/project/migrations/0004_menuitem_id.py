# Generated by Django 4.1.5 on 2023-02-13 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_alter_order_status_alter_order_timeoforder'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='ID',
            field=models.IntegerField(null=True),
        ),
    ]