# Generated by Django 4.1.5 on 2023-01-27 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_modelo_tareas_del_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='modelo_tareas_del_project',
            name='done',
            field=models.BooleanField(default=False),
        ),
    ]