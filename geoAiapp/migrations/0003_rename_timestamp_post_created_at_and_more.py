# Generated by Django 5.1.3 on 2024-12-09 15:37

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geoAiapp', '0002_customuser'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='timestamp',
            new_name='created_at',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='timestamp',
        ),
        migrations.RemoveField(
            model_name='post',
            name='category',
        ),
        migrations.AddField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=255),
        ),
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
