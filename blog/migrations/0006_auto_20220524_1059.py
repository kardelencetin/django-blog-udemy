# Generated by Django 3.1.5 on 2022-05-24 10:59

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_yazilarmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yazilarmodel',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
