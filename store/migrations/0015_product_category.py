# Generated by Django 3.1.1 on 2020-09-07 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_auto_20200907_1315'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]