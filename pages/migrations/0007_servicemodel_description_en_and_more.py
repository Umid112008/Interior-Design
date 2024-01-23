# Generated by Django 5.0.1 on 2024-01-14 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_aboutmodel_description_ru_aboutmodel_title_ru'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicemodel',
            name='description_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='servicemodel',
            name='description_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='servicemodel',
            name='description_uz',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='servicemodel',
            name='title_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='servicemodel',
            name='title_ru',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='servicemodel',
            name='title_uz',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
