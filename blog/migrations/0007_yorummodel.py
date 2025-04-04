# Generated by Django 3.1.5 on 2022-05-24 13:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0006_auto_20220524_1059'),
    ]

    operations = [
        migrations.CreateModel(
            name='YorumModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yorum', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('yazan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='yorum', to=settings.AUTH_USER_MODEL)),
                ('yazi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='yorumlar', to='blog.yazilarmodel')),
            ],
            options={
                'verbose_name': 'yorum',
                'verbose_name_plural': 'yorumlar',
                'db_table': 'yorum',
            },
        ),
    ]
