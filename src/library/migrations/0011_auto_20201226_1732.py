# Generated by Django 3.1.4 on 2020-12-26 17:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_profile_slug'),
        ('library', '0010_commint'),
    ]

    operations = [
        migrations.AlterField(
            model_name='views',
            name='viewer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='viwer', to='profiles.profile', verbose_name='The Viewer'),
        ),
    ]
