# Generated by Django 2.2.16 on 2020-09-22 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_userconfig'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userconfig',
            name='user',
        ),
        migrations.AlterField(
            model_name='userconfig',
            name='dating_gender',
            field=models.BooleanField(choices=[(1, 'male'), (0, 'female')], default=0, help_text='匹配性别', verbose_name='性别'),
        ),
    ]
