from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils.text import slugify
from django_countries.fields import CountryField


class Customer(models.Model):
    user = models.OneToOneField(User,null=True,blank=True,on_delete=models.CASCADE)
    address = models.CharField(max_length=200,null=False)
    address2 = models.CharField(null=True,blank=True,max_length=200)
    country = CountryField()
    city = models.CharField(max_length=200,null=False)
    state = models.CharField(max_length=200,null=False)
    phone_number = models.CharField(default='+',max_length=20,null=False,verbose_name="Mobile Phone Number")
    zipcode = models.CharField(max_length=200,null=False,verbose_name="Zip code")
    image = models.ImageField(null=True ,blank=True,verbose_name="Profile Image")
    image_Cover = models.ImageField(null=True ,blank=True,verbose_name="Profile Cover")
    Bio = models.TextField(max_length=605,null=False,blank=True,verbose_name="Bio Or Stuts")
    ORDER_NOTES = models.TextField(max_length=605,null=False,blank=True,verbose_name="ORDER NOTES")
    slug = models.SlugField(blank=True,null=True,max_length=1000)
    def __str__(self):
        return str(self.user)
    
    # def save(self,*args, **kwargs):
    #     y = self.zipcode
    #     x = int('100080000')
    #     z = str('id-')
    #     c = str('-name-')
    #     f = str('-profile-page')
    #     r = int(y) * int (x)
    #     self.slug = slugify(str(z)+str('1')+ str(r)+ str(c) +str(self.user) + str(f) + str('_flp') )
    #     super(Customer,self).save(*args, **kwargs)


        
    @property
    def image_CoverURL(self):
        try:
            url = self.image_Cover.url
        except:
            url = ''
        return url
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    
@receiver(post_save,sender=User)
def create_user_Customer(sender,instance,created,**kwargs):
    if created:
        Customer.objects.create(user=instance)


