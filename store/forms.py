from django import forms 
from .models import Product,comment
from store.models import ContactModel, MainComment
from accounts.models import Customer


class Product_Post_form(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        exclude = ('oner',)
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control','style':'background: #fff;color: #202020;'}),
            'Brand': forms.TextInput(attrs={'class':'form-control','style':'float:right;width: 200px;background: #fff;color: #202020;outline: none;'}),
            'price': forms.NumberInput(attrs={'class':'form-control','style':'float:right;width: 200px;background: #fff;color: #202020;outline: none;'}),
            'Discountprice': forms.NumberInput(attrs={'class':'form-control','style':'float:right;width: 200px;background: #fff;color: #202020;outline: none;'}),
            'ISNew': forms.NullBooleanSelect(attrs={'class':'form-control','style':'float:right;width: 200px;background: #fff;color: #000;outline: none;'}),
            'ISBestseller': forms.NullBooleanSelect(attrs={'class':'form-control','style':'float:right;width: 200px;background: #fff;color: #000;outline: none;'}),
            'digital': forms.NullBooleanSelect(attrs={'class':'form-control','style':'float:right;width: 200px;background: #fff;color: #000;outline: none;'}),
            'discraption': forms.Textarea(attrs={'class':'form-control','style':'height: 206px;width: 100%;background: #fff;color: #202020;font-family: cursive;font-size: 24px;'}),
            'category': forms.Select(attrs={'class':'form-control','style':'float:right;width: 200px;background: #fff;color: #000;outline: none;'}),
            'image': forms.ClearableFileInput(attrs={'class':'form-control','style':'font-size: 0px;width: 19%;background: #888;color: #888;position: absolute;top: 48%;left: 40%;border-radius: 50%;border: #888;'}),
            'image1': forms.ClearableFileInput(attrs={'class':'form-control','style':'font-size: 0px;width: 19%;background: #888;color: #888;position: absolute;top: 49%;left: 40%;border-radius: 50%;border: #888;height: 10%;'}),
            'image2': forms.ClearableFileInput(attrs={'class':'form-control','style':'font-size: 0px;width: 19%;background: #888;color: #888;position: absolute;top: 49%;left: 40%;border-radius: 50%;border: #888;height: 10%;'}),
            'image3': forms.ClearableFileInput(attrs={'class':'form-control','style':'font-size: 0px;width: 19%;background: #888;color: #888;position: absolute;top: 49%;left: 40%;border-radius: 50%;border: #888;height: 10%;'}),
            'image4': forms.ClearableFileInput(attrs={'class':'form-control','style':'font-size: 0px;width: 19%;background: #888;color: #888;position: absolute;top: 49%;left: 40%;border-radius: 50%;border: #888;height: 10%;'}),     
        }
class commentForm(forms.ModelForm):
    class Meta:
        model = comment
        fields = ['comment','reat']
        widgets = {
            'comment': forms.Textarea(attrs={'class':'form-control','style':'border: 1px solid #e8e8e8;background: transparent;height: 200px;'}),
            'reat': forms.Select(attrs={'class':'form-control','style':'border: 1px solid #e8e8e8;background: transparent;height: 45px;'}),       
        }

class MainCommentForm(forms.ModelForm):
    class Meta:
        model = MainComment
        fields = ['comment']
        widgets = {
            'comment': forms.Textarea(attrs={'class':'form-control','style':'border: 1px solid #e8e8e8;background: transparent;height: 100px;'}), 
        }



class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = '__all__'
        exclude = ('Date',)
        widgets = {
            'Name': forms.TextInput(attrs={'class':'form-control','style':
            "",'placeholder':"Name"}),
            'Subject': forms.TextInput(attrs={'class':'form-control','style':
            "",'placeholder':"Subject"}),
            'Email': forms.EmailInput(attrs={'class':'form-control','style':
            "",'placeholder':"Email"}),
            'Message': forms.Textarea(attrs={'class':'form-control','style':
            "",'placeholder':"Your Message"}),
        }


class UserInfoForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ('slug','user','Bio','image_Cover','image',)
        widgets = {
            'country': forms.Select(attrs={'class':'form-control','style':''}),
            'city': forms.TextInput(attrs={'class':'form-control','style':''}),
            'state': forms.TextInput(attrs={'class':'form-control','style':''}),
            'phone_number': forms.TextInput(attrs={'class':'form-control','style':''}),
            'address': forms.TextInput(attrs={'class':'form-control','style':''}),
            'zipcode': forms.TextInput(attrs={'class':'form-control','style':''}),
            'ORDER_NOTES': forms.Textarea(attrs={'class':'form-control','style':'min-height: 120px;background-color: #f7f7f7;border-color: #f7f7f7;padding: 20px;color: #1f2226;font-size: 13px;','placeholder':'Notes about your order, e.g. special notes for delivery.'}),
        }