# Generated by Django 2.0 on 2020-03-29 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20200329_0006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='data',
            field=models.DateField(auto_now_add=True, verbose_name='创建日期'),
        ),
    ]
