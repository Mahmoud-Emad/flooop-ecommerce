# Generated by Django 3.1.1 on 2020-09-12 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0026_auto_20200912_1921'),
    ]

    operations = [
        migrations.AddField(
            model_name='catdetail',
            name='name',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
