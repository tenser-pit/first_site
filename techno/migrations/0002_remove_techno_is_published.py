# Generated by Django 3.0 on 2022-12-19 17:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('techno', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='techno',
            name='is_published',
        ),
    ]
