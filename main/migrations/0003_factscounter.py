# Generated by Django 3.2 on 2022-11-10 09:54

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20221104_0922'),
    ]

    operations = [
        migrations.CreateModel(
            name='FactsCounter',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=150, verbose_name='title')),
                ('icon_image', models.ImageField(upload_to='facts-counter/', verbose_name='icon image')),
                ('count', models.PositiveIntegerField(verbose_name='count')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
            ],
            options={
                'verbose_name': 'Facts Counter',
                'verbose_name_plural': 'Facts Counter',
            },
        ),
    ]
