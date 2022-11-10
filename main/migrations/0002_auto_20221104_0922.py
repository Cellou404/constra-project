# Generated by Django 3.2 on 2022-11-04 09:22

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='detail',
            field=tinymce.models.HTMLField(verbose_name='detail'),
        ),
        migrations.AlterField(
            model_name='service',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, null=True, unique=True, verbose_name='slug'),
        ),
    ]
