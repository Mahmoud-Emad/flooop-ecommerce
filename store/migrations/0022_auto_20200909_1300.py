# Generated by Django 3.1.1 on 2020-09-09 11:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0021_auto_20200909_1149'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='email',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='name',
        ),
    ]