# Generated by Django 3.1.4 on 2020-12-18 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_auto_20201217_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='library',
            name='content',
            field=models.FileField(upload_to=''),
        ),
    ]