# Generated by Django 4.2.7 on 2023-11-11 16:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_alter_dish_cooks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='dish_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dishes', to='restaurant.dishtypes'),
        ),
    ]
