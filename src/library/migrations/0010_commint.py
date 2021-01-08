# Generated by Django 3.1.4 on 2020-12-22 14:25

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_profile_slug'),
        ('library', '0009_views'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=200)),
                ('created', models.DateField(default=datetime.datetime.now)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.library')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.profile')),
            ],
        ),
    ]