# Generated by Django 3.1.4 on 2020-12-18 12:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0006_auto_20201218_1209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='library',
            name='content',
            field=models.FileField(upload_to='', verbose_name=django.core.validators.FileExtensionValidator(['pdf'])),
        ),
    ]
