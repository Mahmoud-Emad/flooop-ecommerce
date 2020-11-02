# Generated by Django 3.1.1 on 2020-09-27 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0047_auto_20200927_2144'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='reat1',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='reat2',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='reat3',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='reat4',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='reat5',
        ),
        migrations.AddField(
            model_name='comment',
            name='reat',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default='', max_length=255),
            preserve_default=False,
        ),
    ]