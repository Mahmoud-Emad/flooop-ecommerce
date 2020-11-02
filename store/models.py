from django.db import models
from django.contrib.auth.models import User
from django.urls.base import reverse
from django.db.models.signals import post_save

from django.utils.text import slugify
from accounts.models import Customer
import random




class category(models.Model):
    name = models.CharField(max_length=255)
    Title = models.CharField(max_length=255)
    Image = models.ImageField(max_length=1000,null=True ,blank=True,verbose_name="Category Image")
    
    def __str__(self):
        return self.name
    def get_absolute_url (self):
        return reverse('store')  


choice_list = (
    ('Arts and Crafts','Arts and Crafts'),
    ('Automotive','Automotive'),
    ('Baby','Baby'),
    ('Beauty Personal Care','Beauty Personal Care'),
    ('Books','Books'),
    ('Boys Fashion','Boys Fashion'),
    ('Computers','Computers'),
    ('Clothes','Clothes'),
    ('Dance sport','Dance sport'),
    ('Electronics','Electronics'),
    ('Girls Fashion','Girls Fashion'),
    ('Health and Household','Health and Household'),
    ('Home and Kitchen','Home and Kitchen'),
    ('Industrial and Scientific','Industrial and Scientific'),
    ('Luggage','Luggage'),
    ('Music or CDs and Vinyl','Music or CDs and Vinyl'),
    ('Movies','Movies'),
    ('Mens Fashion','Mens Fashion'),
    ('Phone and accessories','Phone and accessories'),
    ('Pet Supplies','Pet Supplies'),
    ('Software','Software'),
    ('Sports and Outdoors','Sports and Outdoors'),
    ('Swimming','Swimming'),
    ('Television','Television'),
    ('Toys and Games','Toys and Games'),
    ('Travel','Travel'),
    ('Tools and Home Improvement','Tools and Home Improvement'),
    ('Video Games','Video Games'),
    ('Womens Fashion','Womens Fashion'),

)





class Product(models.Model):
    oner = models.ForeignKey(User,related_name='product_owner',on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=7,decimal_places=2)
    Discountprice = models.DecimalField(max_digits=7,decimal_places=2,blank=True,null=True,verbose_name=("Discount Price"))
    ISNew = models.BooleanField(default=True,verbose_name=("New Product"))
    ISBestseller = models.BooleanField(default=False,verbose_name=("Best seller"))
    digital = models.BooleanField(default=False,null=True,blank=True)
    discraption = models.TextField(max_length=1000,null=True,blank=True,verbose_name="discraption")
    category = models.CharField(choices=choice_list,max_length=255)
    Brand = models.CharField(max_length=200,null=True ,blank=True,)
    image = models.ImageField(max_length=1000,null=True ,blank=True,verbose_name="Top Image")
    image1 = models.ImageField(max_length=1000,null=True ,blank=True,verbose_name="More Image")
    image2 = models.ImageField(max_length=1000,null=True ,blank=True,verbose_name="More Image")
    image3 = models.ImageField(max_length=1000,null=True ,blank=True,verbose_name="More Image")
    image4 = models.ImageField(max_length=1000,null=True ,blank=True,verbose_name="More Image")
    slug = models.SlugField(blank=True,null=True,max_length=1000)
    offer = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name + ' | #In Category Of ( ' + self.category +' ) ' + '  --->  ' + str(self.oner)


    def get_amount_saved(self):
        return int(self.price) - int(self.Discountprice)
    
    def save(self,*args, **kwargs):
        y = self.price
        x = int('100080000')
        z = str('id-')
        c = str('-name-')
        f = str('-404-f5S')
        r = int(y) * int (x)
        self.slug = slugify(str(z)+str('1')+ str(r)+ str(c) +str(self.name) + str('_') + str(self.Brand)+ str(f))
        super(Product,self).save(*args, **kwargs)

        
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    


class Recommendations_for_you(models.Model):
    name = models.CharField(max_length=200)
    image1 = models.ImageField(null=True ,blank=True,verbose_name="More Image")
    image2 = models.ImageField(null=True ,blank=True,verbose_name="More Image")
    image3 = models.ImageField(null=True ,blank=True,verbose_name="More Image")
    image4 = models.ImageField(null=True ,blank=True,verbose_name="More Image")
    category = models.CharField(choices=choice_list,max_length=255)

    def __str__(self):
        return self.name

class Our_Department(models.Model):
    Name = models.CharField(max_length=200)
    One = models.CharField(choices=choice_list,max_length=255)
    Two = models.CharField(choices=choice_list,max_length=255)
    Three = models.CharField(choices=choice_list,max_length=255)
    Four = models.CharField(choices=choice_list,max_length=255)
    Five = models.CharField(choices=choice_list,max_length=255)

    def __str__(self):
        return self.Name



rate_list = (
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
    ('5','5'),
)

class comment(models.Model):
    reat = models.CharField(choices=rate_list,max_length=255)
    name = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Product,on_delete=models.CASCADE)
    comment = models.TextField(max_length=605,null=False,blank=True,verbose_name="Comment")
    date_added = models.DateTimeField(auto_now=True)
    def __str__(self):
        return '{} - {}'.format (self.post.name , str(self.name))


class MainComment(models.Model):
    name = models.ForeignKey(User,on_delete=models.CASCADE)
    comment = models.TextField(max_length=605,null=False,blank=True,verbose_name="Comment")
    
    def __str__(self):
        return str(self.name)

class Order(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True,blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(max_length=100,null=True,blank=True)
    transaction_id = models.CharField(max_length=200,null=True)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems ])
        return total
    
    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems ])
        return total
    
    @property
    def shipping(self):
        shipping = False
        orderitem = self.orderitem_set.all()
        for i in orderitem:
            if i.product.digital == False:
                shipping = True
        return shipping

class OrderItem(models.Model):
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,blank=True,null=True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL,blank=True,null=True)
    quantity = models.IntegerField(default=0,null=True,blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.product
    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total


class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL,blank=True,null=True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL,blank=True,null=True)
    address = models.CharField(max_length=200,null=False)
    city = models.CharField(max_length=200,null=False)
    state = models.CharField(max_length=200,null=False)
    phone_number = models.CharField(max_length=20,null=False)
    zipcode = models.CharField(max_length=200,null=False)
    date_added = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.address  


class Swiber_bags(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(max_length=1000,null=True ,blank=True,verbose_name="Image Of Product")
    category = models.CharField(choices=choice_list,max_length=255)

    def __str__(self):
        return self.name 


class ContactModel(models.Model):
    Name = models.CharField(max_length=250,verbose_name='Name Of User')
    Subject = models.CharField(max_length=350,verbose_name='Subject Of User')
    Email  = models.EmailField(max_length=350,verbose_name='Email Of User')
    Message  = models.TextField(max_length=1000,verbose_name='Message Of User')
    Date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.Name) + str(" < | > ") + str(self.Email)

class BannerEvryWeak(models.Model):
    Text = models.CharField(max_length=250,verbose_name='Short text about section')
    HashTag = models.CharField(max_length=250, null=True,blank=True ,verbose_name='Hash Tag Important ')
    category = models.CharField(choices=choice_list,max_length=255)

    def __str__(self):
        return str(self.Text) + str(" < | > ") + str(self.category)


