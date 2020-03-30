# Generated by Django 2.0 on 2020-03-30 02:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_auto_20200329_2354'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=50, verbose_name='昵称')),
                ('content', models.TextField(verbose_name='内容')),
                ('date', models.DateField(auto_now_add=True, verbose_name='评论时间')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.Article', verbose_name='文章')),
            ],
            options={
                'verbose_name': '评论表',
                'verbose_name_plural': '评论表',
                'db_table': 'comment',
            },
        ),
    ]