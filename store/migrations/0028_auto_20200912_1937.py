# Generated by Django 3.1.1 on 2020-09-12 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0027_catdetail_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Catdetail',
        ),
        migrations.AddField(
            model_name='category',
            name='head_titel',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='titel',
            field=models.TextField(default='', max_length=1000),
            preserve_default=False,
        ),
    ]
