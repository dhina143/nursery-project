# Generated by Django 4.2.5 on 2024-01-11 05:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drive', '0009_navbar_alter_dropdownitem_title_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='navbar',
            name='url',
        ),
    ]