# Generated by Django 3.1.5 on 2022-05-24 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20220520_1346'),
    ]

    operations = [
        migrations.RenameField(
            model_name='kategorimodel',
            old_name='slug',
            new_name='kategori_slug',
        ),
    ]
