# Generated by Django 2.2.7 on 2020-02-04 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_comment_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='description1',
            field=models.TextField(default=1, max_length=470, verbose_name='المحتوى'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='description2',
            field=models.TextField(default=1, max_length=470, verbose_name='المحتوى'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='most_advanced',
            field=models.TextField(default=1, max_length=470, verbose_name='المحتوى'),
            preserve_default=False,
        ),
    ]
