from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from accounts.models import Customer




class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']

class LOGIN_FORM(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password']


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ('slug','user','ORDER_NOTES')
        widgets = {
            'country': forms.Select(attrs={'class':'form-control','style':'background-color: rgb(250, 242, 242);width:60%;height: 41px;float: right;'}),
            'city': forms.TextInput(attrs={'class':'form-control','style':'background-color: rgb(250, 242, 242);width:60%;height: 33px;float: right;'}),
            'state': forms.TextInput(attrs={'class':'form-control','style':'background-color: rgb(250, 242, 242);width:60%;height: 33px;float: right;'}),
            'phone_number': forms.TextInput(attrs={'class':'form-control','style':'background-color: rgb(250, 242, 242);width:60%;height: 33px;float: right;'}),
            'Bio': forms.Textarea(attrs={'class':'form-control','style':'background-color: rgb(250, 242, 242);height: 197px;'}),
            'address': forms.TextInput(attrs={'class':'form-control','style':'background-color: rgb(250, 242, 242);width:60%;height: 33px;float: right;'}),
            'zipcode': forms.TextInput(attrs={'class':'form-control','style':'background-color: rgb(250, 242, 242);width:60%;height: 33px;float: right;'}),
            'image_Cover': forms.ClearableFileInput(attrs={'class':'form-control','style':
            "padding-left: 29px;height: 64px;background-repeat: no-repeat;width: 76px;font-size: 0px;background-size: 75px;background-image: url(/static/images/camira.jpg)"}),
            'image': forms.ClearableFileInput(attrs={'class':'form-control','style':
            "padding-left: 29px;height: 64px;background-repeat: no-repeat;width: 76px;font-size: 0px;background-size: 75px;background-image: url(/static/images/camira.jpg)"}),
        }



class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control', 'type' : 'password','placeholder' : 'Old Password'}))
    new_password1 = forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'class' : 'form-control', 'type' : 'password','placeholder' : 'New Password'}))
    new_password2 = forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'class' : 'form-control', 'type' : 'password','placeholder' : 'Re-Enter New Password'}))
    class Meta:
        model = User
        fields = ('old_password','new_password1','new_password2')