# Generated by Django 3.1.4 on 2020-12-18 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0007_auto_20201218_1210'),
    ]

    operations = [
        migrations.AddField(
            model_name='library',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]
