# Generated by Django 5.0.7 on 2024-08-22 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gastos',
            name='valor',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
