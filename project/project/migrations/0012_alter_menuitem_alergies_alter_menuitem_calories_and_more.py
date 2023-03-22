# Generated by Django 4.1.5 on 2023-03-22 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0011_alter_menuitem_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='alergies',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='calories',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]