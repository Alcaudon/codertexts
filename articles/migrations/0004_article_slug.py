# Generated by Django 2.0.3 on 2018-04-02 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20180325_1242'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]
