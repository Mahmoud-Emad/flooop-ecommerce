# Generated by Django 3.1.1 on 2020-10-25 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20200926_0409'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='ORDER_NOTES',
            field=models.TextField(blank=True, max_length=605, verbose_name='ORDER NOTES'),
        ),
    ]
