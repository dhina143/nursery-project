# Generated by Django 4.2.5 on 2024-02-01 12:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drive', '0023_rename_dropdown_category_alter_category_options_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='NavItem',
            new_name='SubCategory',
        ),
        migrations.AlterModelOptions(
            name='subcategory',
            options={'verbose_name_plural': 'SubCategory'},
        ),
        migrations.AlterModelTable(
            name='subcategory',
            table='SubCategory',
        ),
    ]