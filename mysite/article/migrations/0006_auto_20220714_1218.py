# Generated by Django 2.1.5 on 2022-07-14 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_article_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='article',
            name='readed_num',
            field=models.IntegerField(default=0),
        ),
    ]
