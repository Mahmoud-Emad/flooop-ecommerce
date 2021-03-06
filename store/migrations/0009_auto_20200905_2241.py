# Generated by Django 3.1.1 on 2020-09-05 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_auto_20200905_2237'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='name',
        ),
        migrations.AddField(
            model_name='category',
            name='CATImg',
            field=models.ImageField(default='', upload_to='category/', verbose_name='image'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='CATName',
            field=models.CharField(default='', max_length=50, verbose_name='Name'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Arts & Crafts', 'Arts & Crafts'), ('Automotive', 'Automotive'), ('Baby', 'Baby'), ('Beauty & Personal Care', 'Beauty & Personal Care'), ('Swimming', 'Swimming'), ('Wrestling', 'Wrestling'), ('Tv', 'Tv'), ('Books', 'Books'), ('Electronics', 'Electronics'), ('Computers', 'Computers'), ("Women's Fashion", "Women's Fashion"), ("Men's Fashion", "Men's Fashion"), ("Girls' Fashion", "Girls' Fashion"), ("Boys' Fashion", "Boys' Fashion"), ('Health & Household', 'Health & Household'), ('Home & Kitchen', 'Home & Kitchen'), ('Industrial & Scientific', 'Industrial & Scientific'), ('Luggage', 'Luggage'), ('Movies & Television', 'Movies & Television'), ('Music, CDs & Vinyl', 'Music, CDs & Vinyl'), ('Pet Supplies', 'Pet Supplies'), ('Software', 'Software'), ('Sports & Outdoors', 'Sports & Outdoors'), ('Tools & Home Improvement', 'Tools & Home Improvement'), ('Toys & Games', 'Toys & Games'), ('Video Games', 'Video Games'), ('Phone&Accsessoaris', 'Video Games')], max_length=30),
        ),
    ]
