# Generated by Django 3.2 on 2022-11-02 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='projects/thumbnail/%Y/%m/%d/', verbose_name='thumbnail'),
        ),
    ]