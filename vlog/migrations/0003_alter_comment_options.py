# Generated by Django 4.2.17 on 2025-01-12 15:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vlog', '0002_alter_video_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['created_at']},
        ),
    ]
