# Generated by Django 3.2.4 on 2022-06-11 10:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todolist',
            name='content',
        ),
        migrations.AlterField(
            model_name='todolist',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='todos.category'),
        ),
    ]
