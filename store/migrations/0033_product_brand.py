# Generated by Django 3.1.1 on 2020-09-18 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0032_auto_20200917_1230'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Brand',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]