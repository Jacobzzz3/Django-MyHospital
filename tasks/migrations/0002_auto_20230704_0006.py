# Generated by Django 3.0.14 on 2023-07-04 04:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='descripcion',
            new_name='reseña',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='title',
            new_name='titulo',
        ),
        migrations.RemoveField(
            model_name='task',
            name='important',
        ),
        migrations.AddField(
            model_name='task',
            name='ubicacion',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
    ]
