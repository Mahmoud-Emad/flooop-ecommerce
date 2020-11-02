# Generated by Django 3.1.1 on 2020-09-09 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0020_auto_20200907_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('books', 'books'), ('Arts and Crafts', 'Arts and Crafts'), ('Automotive', 'Automotive'), ('Baby', 'Baby'), ('Beauty Personal Care', 'Beauty Personal Care'), ('Swimming', 'Swimming'), ('Wrestling', 'Wrestling'), ('Television', 'Television'), ('Books', 'Books'), ('Electronics', 'Electronics'), ('Computers', 'Computers'), ("Women's Fashion", "Women's Fashion"), ('Mens Fashion', 'Mens Fashion'), ('Girls Fashion', 'Girls Fashion'), ('Boys Fashion', 'Boys Fashion'), ('Health and Household', 'Health and Household'), ('Home and Kitchen', 'Home and Kitchen'), ('Industrial and Scientific', 'Industrial and Scientific'), ('Luggage', 'Luggage'), ('Movies', 'Movies'), ('Music or CDs and  Vinyl', 'Music or CDs and  Vinyl'), ('Pet Supplies', 'Pet Supplies'), ('Software', 'Software'), ('Sports and Outdoors', 'Sports and Outdoors'), ('Tools and Home Improvement', 'Tools and Home Improvement'), ('Toys and Games', 'Toys and Games'), ('Video Games', 'Video Games'), ('Phone and accessories', 'Phone and accessories'), ('Travel', 'Travel'), ('Dance sport', 'Dance sport'), ('Clothes', 'Clothes')], max_length=255),
        ),
    ]