# Generated by Django 5.0.1 on 2024-01-13 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_aboutmodel_description_en_aboutmodel_description_uz_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutmodel',
            name='description_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='aboutmodel',
            name='title_ru',
            field=models.CharField(max_length=255, null=True),
        ),
    ]