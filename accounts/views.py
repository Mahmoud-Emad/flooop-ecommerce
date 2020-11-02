from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm,PasswordChangingForm
from django.contrib import messages
from store.utils import cartData
from store.models import category
from django.contrib.auth import authenticate, login , logout
from store.models import *
from store.views import *
from django.urls.base import reverse_lazy, reverse
from django.contrib.auth.views import PasswordChangeView
from accounts.forms import EditProfileForm
from django.views.generic.edit import CreateView
from accounts.models import Customer
from django.views import generic



class ViweProfilePage(CreateView):
    model = Customer
    fields = '__all__'
    template_name = 'profile.html'

    def get(self, request, *args, **kwargs):
        profile = Customer.objects.all()
        page_user = get_object_or_404(Customer,id=self.kwargs['pk'])
        data= cartData(request)
        cartItems = data['cartItems']
        items = data['items']
        order = data['order']
        cat_menu = category.objects.all()
        return render(request, self.template_name, {
        'cartItems':cartItems,
        'items':items,
        'order':order,
        'cat_menu':cat_menu,
        'page_user':page_user,
        })





class EditProfilePageView(generic.UpdateView):
    model = Customer
    template_name = 'ProfileEdit.html'
    form_class  = EditProfileForm

    def get(self, request, *args, **kwargs):
        profile_edit = Customer.objects.get(user=request.user)
        form = self.form_class(request.POST,request.FILES,instance=profile_edit)
        if request.method == 'POST':
            if form.is_valid():
                form = EditProfileForm(request.POST,instance=profile_edit)
                myprofile = form.save(commit=False)
                myprofile.user = request.user
                myprofile.save()
                return redirect(reverse('profile'))
        else:
            form = EditProfileForm(instance=profile_edit)
            
        data= cartData(request)
        cartItems = data['cartItems']
        items = data['items']
        order = data['order']
        cat_menu = category.objects.all()
        return render(request, self.template_name, {'profile_edit':profile_edit,
        'form':form,
        'cartItems':cartItems,
        'items':items,
        'order':order,
        'cat_menu':cat_menu,
        })


    def get_success_url(self):
        companyid=self.kwargs['pk']
        return reverse_lazy('user_profile_page', kwargs={'pk': companyid})



def ProfileViwe(request):
    data= cartData(request)
    cartItems = data['cartItems']
    items = data['items']
    order = data['order']
    
    cat_menu = category.objects.all()
    context= {'cartItems':cartItems,'cat_menu':cat_menu,
    'items':items,'order':order}
    return render (request, "profile.html",context)





def RegisterView(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,"You'r one of our family now dear { " + user + ' }')
            return redirect('login')
            
    context = {'form':form}
    return render (request,'registration/register.html',context)


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    success_url = reverse_lazy('password_change_done')
    template_name = ('registration/change_password.html')

def Conditions_of_Use(request):
    context = {}
    return render (request,'Conditions_of_Use.html',context)

def Covid(request):
    context = {}
    return render (request,'Covid.html',context)

def GetProductHelp(request):
    data= cartData(request)
    cartItems = data['cartItems']
    items = data['items']
    order = data['order']
    products = Product.objects.all()
    item_cat = Recommendations_for_you.objects.all()
    swip = Swiber_bags.objects.all()
    cat_menu = category.objects.all()
    myfilter = ProductFilter(request.GET,queryset=products)
    products = myfilter.qs
    paginator = Paginator(products, 11) # Show 25 contacts per page.
    page = request.GET.get('page')
    Page_number = paginator.get_page(page)
    context= {'products':Page_number,'cartItems':cartItems,'cat_menu':cat_menu,
    'item_cat':item_cat,'swip':swip,'myfilter':myfilter,'items':items,'order':order}
    return render (request,'Get_product_help.html',context)

def Privcy(request):
    context = {}
    return render (request,'Privcy.html',context)
