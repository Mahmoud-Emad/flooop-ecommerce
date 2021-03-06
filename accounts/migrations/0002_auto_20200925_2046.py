# Generated by Django 3.1.1 on 2020-09-25 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='address',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='address2',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='city',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='phone_number',
            field=models.CharField(default='+', max_length=20),
        ),
        migrations.AddField(
            model_name='customer',
            name='state',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='zipcode',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
