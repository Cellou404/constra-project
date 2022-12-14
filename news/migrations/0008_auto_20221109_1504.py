# Generated by Django 3.2 on 2022-11-09 15:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_auto_20221109_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archive',
            name='date',
            field=models.CharField(blank=True, help_text='Please use this format: November 2021', max_length=16, null=True, verbose_name='date'),
        ),
        migrations.AlterField(
            model_name='post',
            name='year_completed',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='news.archive', verbose_name='year completed'),
        ),
    ]
