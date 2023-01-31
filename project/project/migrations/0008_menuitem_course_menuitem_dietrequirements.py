# Generated by Django 4.1.5 on 2023-01-25 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0007_alter_order_customerid'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='course',
            field=models.CharField(choices=[('Starter', 'Starter'), ('Main', 'Main'), ('Dessert', 'Dessert'), ('Side', 'Side'), ('Drink', 'Drink')], default='Main', max_length=10),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='dietRequirements',
            field=models.BooleanField(choices=[('Vegan', 'Vegan'), ('Vegetarian', 'Vegetarian')], max_length=10, null=True),
        ),
    ]
