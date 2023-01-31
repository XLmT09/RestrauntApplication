# Generated by Django 4.1.5 on 2023-01-21 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_rename_menu_menuitem_alter_menuitem_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('customerID', models.IntegerField()),
                ('status', models.CharField(choices=[('Placed', 'Placed'), ('Confirmed', 'Confirmed'), ('Delivered', 'Delivered')], max_length=10)),
                ('timeOfOrder', models.TimeField()),
            ],
            options={
                'db_table': 'Order',
            },
        ),
    ]
