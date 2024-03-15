# Generated by Django 5.0.1 on 2024-02-06 11:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drive', '0028_remove_items_item_img_alter_items_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='drive.category'),
        ),
        migrations.AlterField(
            model_name='items',
            name='navbar',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='drive.navbar'),
        ),
        migrations.AlterField(
            model_name='items',
            name='subcategory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='drive.subcategory'),
        ),
    ]