from django.shortcuts import render, redirect
from .models import *

from django.http.response import JsonResponse, HttpResponseBadRequest,\
    HttpResponseRedirect
import json
import datetime
from . utils import cookieCart,cartData,geustOrder
from django.core.paginator import Paginator
from django.views.generic import CreateView
from .forms import Product_Post_form
from .filters import ProductFilter
from django.urls.base import reverse_lazy
from store.forms import commentForm, ContactForm, MainCommentForm
from django.contrib.auth.decorators import login_required
import random


def Category_Home(request):
    mydate = datetime.datetime.now()
    Shop_list = Our_Department.objects.all()
    data= cartData(request)
    items = data['items']
    order = data['order']
    cartItems = data['cartItems']
    all_department = category.objects.all()
    context={
        'all_department':all_department,
        'Shop_list':Shop_list,
        'items':items,
        'order':order,
        'cartItems':cartItems,
        'mydate':mydate,
        }
    return render (request,'Category.html',context)    


def floop_basic(request):
    mydate = datetime.datetime.now()
    Shop_list = Our_Department.objects.all()
    data= cartData(request)
    items = data['items']
    order = data['order']
    cartItems = data['cartItems']
    products = Product.objects.all()
    myfilter = ProductFilter(request.GET,queryset=products)
    products = myfilter.qs
    item_cat = Recommendations_for_you.objects.all()
    swip = Swiber_bags.objects.all()
    cat_menu = category.objects.all()
    context= {'products':products,'myfilter':myfilter,'swip':swip,'cat_menu':cat_menu,'cartItems':cartItems,'item_cat':item_cat,'items':items,'order':order,
    'Shop_list':Shop_list,"mydate":mydate}
    return render (request, "store/floop_basic.html",context)

def Customer_sirves(request):
    Shop_list = Our_Department.objects.all()
    today = datetime.date.today()
    mydate = datetime.datetime.now()
    data= cartData(request)
    items = data['items']
    order = data['order']
    cartItems = data['cartItems']
    products = Product.objects.all()
    myfilter = ProductFilter(request.GET,queryset=products)
    products = myfilter.qs
    item_cat = Recommendations_for_you.objects.all()
    swip = Swiber_bags.objects.all()
    cat_menu = category.objects.all()
    context= {'products':products,'myfilter':myfilter,'swip':swip,'cat_menu':cat_menu,'cartItems':cartItems,
    'item_cat':item_cat,'items':items,'order':order,'today':today,'mydate':mydate,
    'Shop_list':Shop_list}
    return render (request, "Customer_sirves.html",context)

def Offer_day(request):
    Shop_list = Our_Department.objects.all()
    data= cartData(request)
    cartItems = data['cartItems']
    items = data['items']
    order = data['order']
    today = datetime.date.today()
    mydate = datetime.datetime.now()
    products = Product.objects.filter(offer__icontains = today)
    paginator = Paginator(products, 20) # Show 25 contacts per page.
    page = request.GET.get('page')
    Page_number = paginator.get_page(page)
    context = {'products':Page_number,'mydate':mydate,'today':today,'cartItems':cartItems,'items':items,'order':order,
    'Shop_list':Shop_list}
    return render (request, "Offerday.html",context)





def search(request):
    try:
        q = request.GET.get('q')
    except:
        q = None
    if q:
        mydate = datetime.datetime.now()
        data= cartData(request)
        items = data['items']
        order = data['order']
        products = Product.objects.filter(name__icontains=q)
        item_cat = Recommendations_for_you.objects.all()
        cartItems = data['cartItems']
        cat_menu = category.objects.all()
        template = "result.html"
        paginator = Paginator(products, 1) # Show 25 contacts per page.
        page = request.GET.get('page')
        Page_number = paginator.get_page(page)
        context= {'query':q,'products':products,'item_cat':item_cat,'cartItems':cartItems
            ,'cat_menu':cat_menu
            ,'items':items
            ,'order':order
            ,'mydate':mydate,
            
        }
    else:
        mydate = datetime.datetime.now()
        data= cartData(request)
        items = data['items']
        order = data['order']
        cartItems = data['cartItems']
        products = Product.objects.all()
        item_cat = Recommendations_for_you.objects.all()
        template = "Search.html"
        cat_menu = category.objects.all()
        paginator = Paginator(products, 10) # Show 25 contacts per page.
        page = request.GET.get('page')
        Page_number = paginator.get_page(page)
        swip = Swiber_bags.objects.all()
        context= {'products':Page_number,'cartItems':cartItems,'cat_menu':cat_menu,
            'item_cat':item_cat,
            'swip':swip
            ,'items':items
            ,'order':order
            ,'mydate':mydate,
        }
    return render (request,template ,context)



def Store(request):
    Shop_list = Our_Department.objects.all()
    mydate = datetime.datetime.now()
    banner = BannerEvryWeak.objects.all()
    data= cartData(request)
    cartItems = data['cartItems']
    items = data['items']
    order = data['order']
    item_cat = Recommendations_for_you.objects.all()
    swip = list(Swiber_bags.objects.all())
    swip = random.sample(swip, 20)
    cat_menu = category.objects.all()
    products = list(Product.objects.all())
    products = random.sample(products, 80)
    today = datetime.date.today()
    ProDay = Product.objects.filter(offer__icontains = today)
    mydate = datetime.datetime.now()
    Comments = MainComment.objects.all()
    comment_form = MainCommentForm()
    if request.method == 'POST':
        comment_form = MainCommentForm(request.POST or None)
        if comment_form.is_valid():
            comment_form.save(commit=False)
            commento = request.POST.get('comment')
            Contant = MainComment.objects.create(name=request.user ,comment=commento)
            Contant.save()
            return redirect(reverse('store'))
        else:
            comment_form = commentForm()
    context= {'comment_form':comment_form,'Comments':Comments,
                'mydate':mydate,'ProDay':ProDay,'products':products,
                'cartItems':cartItems,'cat_menu':cat_menu,'mydate':mydate,
                'item_cat':item_cat,'swip':swip,'items':items,'order':order,
                'banner':banner,'count': Product.objects.count(),
                'CountDay':Product.objects.filter(offer__icontains = today).count(),
    'Shop_list':Shop_list
    }
    return render (request, "index.html",context)

def product_deteil(request,slug):
    Shop_list = Our_Department.objects.all()
    mydate = datetime.datetime.now()
    data= cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    product_deteil = Product.objects.get(slug=slug)
    
    cat_menu = category.objects.all()
    items = data['items']
    order = data['order']
    comments = comment.objects.filter(post = product_deteil).order_by('-id')
    comment_form = commentForm()
    if request.method == 'POST':
        comment_form = commentForm(request.POST or None)
        if comment_form.is_valid():
            commento = request.POST.get('comment','reat')
            rear = request.POST.get('reat')
            Contant = comment.objects.create(post = product_deteil,name=request.user ,comment=commento,reat=rear)
            Contant.save()
            return HttpResponseRedirect(product_deteil.slug)
        else:
            comment_form = commentForm()
    context = {
        'product_deteil':product_deteil,
        'items':items,'order':order,
        'cartItems':cartItems,
        'cat_menu':cat_menu,
        'mydate':mydate,
        'items':items,'order':order,
        'comments':comments,'comment_form':comment_form,
    'Shop_list':Shop_list}
    
    return render (request,"product-details.html",context)


def ShopAllIn(request):
    mydate = datetime.datetime.now()
    Shop_list = Our_Department.objects.all()
    banner = BannerEvryWeak.objects.all()
    data= cartData(request)
    cartItems = data['cartItems']
    items = data['items']
    order = data['order']
    products = list(Product.objects.all())
    products = random.sample(products, 80)

    context= {'products':products,'cartItems':cartItems,'items':items,'order':order,'banner':banner,'count': Product.objects.count(),
    'Shop_list':Shop_list,'mydate':mydate}
    return render (request, "All_IN-grid.html",context)

def SHopView(request):
    mydate = datetime.datetime.now()
    Shop_list = Our_Department.objects.all()
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
    paginator = Paginator(products, 21) # Show 25 contacts per page.
    page = request.GET.get('page')
    Page_number = paginator.get_page(page)

    context= {'products':Page_number,'cartItems':cartItems,'cat_menu':cat_menu,
    'item_cat':item_cat,'swip':swip,'myfilter':myfilter,'items':items,'order':order,
    'Shop_list':Shop_list,
    'mydate':mydate}
    return render (request, "shop.html",context)

def Sale_Viwe(request):
    mydate = datetime.datetime.now()
    Shop_list = Our_Department.objects.all()
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
    paginator = Paginator(products, 17) # Show 25 contacts per page.
    page = request.GET.get('page')
    Page_number = paginator.get_page(page)
    context= {'products':Page_number,'cartItems':cartItems,'cat_menu':cat_menu,
    'item_cat':item_cat,'swip':swip,'myfilter':myfilter,'items':items,'order':order,
    'Shop_list':Shop_list,'mydate':mydate}
    return render (request, "store/Sale_page.html",context)


def best_seller(request):
    mydate = datetime.datetime.now()
    Shop_list = Our_Department.objects.all()
    data= cartData(request)
    cartItems = data['cartItems']
    items = data['items']
    order = data['order']
    products = Product.objects.all()
    count = Product.objects.all()
    item_cat = Recommendations_for_you.objects.all()
    swip = Swiber_bags.objects.all()
    cat_menu = category.objects.all()
    myfilter = ProductFilter(request.GET,queryset=products)
    products = myfilter.qs
    paginator = Paginator(products, 16) # Show 25 contacts per page.
    page = request.GET.get('page')
    Page_number = paginator.get_page(page)
    context= {'products':Page_number,'cartItems':cartItems,'cat_menu':cat_menu,
    'item_cat':item_cat,'swip':swip,'myfilter':myfilter,'items':items,'order':order,'count':Product.objects.all().count,
    'Shop_list':Shop_list,'mydate':mydate}
    return render (request, "best_seller.html",context)


def Recommendations(request):
    mydate = datetime.datetime.now()
    Shop_list = Our_Department.objects.all()
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
    paginator = Paginator(products, 21) # Show 25 contacts per page.
    page = request.GET.get('page')
    Page_number = paginator.get_page(page)
    context= {'products':Page_number,'cartItems':cartItems,'cat_menu':cat_menu,
    'item_cat':item_cat,'swip':swip,'myfilter':myfilter,'items':items,'order':order,
    'Shop_list':Shop_list,
    'mydate':mydate}
    return render (request, "Recommendations.html",context)


def CategoryView(request,cats):
    mydate = datetime.datetime.now()
    Shop_list = Our_Department.objects.all()
    data= cartData(request)
    cartItems = data['cartItems']
    items = data['items']
    order = data['order']
    cat_menu = category.objects.all()
    Category_Post = Product.objects.filter(category__iexact=cats.replace('-' ,' '))
    myfilter = ProductFilter(request.GET,queryset=Category_Post)
    products = myfilter.qs
    paginator = Paginator(products, 9) # Show 25 contacts per page.
    page = request.GET.get('page')
    Page_number = paginator.get_page(page)
    return render (request,'shop.html',{'products':Page_number,'cats':cats.title().replace('-',' ') ,
     'Category_Post':Category_Post,'cat_menu':cat_menu,'cat_menu':cat_menu,'cartItems':cartItems,'items':items,'order':order,
    'mydate':mydate,
    'Shop_list':Shop_list})



@login_required
def Post_product(request):
    Shop_list = Our_Department.objects.all()
    mydate = datetime.datetime.now()
    data= cartData(request)
    items = data['items']
    order = data['order']
    cartItems = data['cartItems']
    cat_menu = category.objects.all()
    if request.method =='POST':
        form_class = Product_Post_form(request.POST,request.FILES)
        if form_class.is_valid():
            myform = form_class.save(commit=False)
            myform.oner = request.user
            myform.save()
            return redirect ('store')
    else:
        form_class = Product_Post_form()
    return render(request,'add_product.html',
    {   'form_class':form_class,'cat_menu':cat_menu,'mydate':mydate,
        'items':items,'order':order,'cartItems':cartItems,
    'Shop_list':Shop_list
    })


def Cart(request):
    mydate = datetime.datetime.now()
    Shop_list = Our_Department.objects.all()
    products = Product.objects.all()
    myfilter = ProductFilter(request.GET,queryset=products)
    products = myfilter.qs
    paginator = Paginator(products, 6) # Show 25 contacts per page.
    page = request.GET.get('page')
    Page_number = paginator.get_page(page)
    data= cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    cat_menu = category.objects.all()
    context= {'items':items,
    'products':Page_number,
    'order':order,
    'cartItems':cartItems,
    'Page_number':Page_number,
    'Page_number':Page_number,
    'cat_menu':cat_menu,
    'mydate':mydate,
    'Shop_list':Shop_list}
    return render (request, "cart-page.html",context)


def Checkout(request):
    mydate = datetime.datetime.now()
    Shop_list = Our_Department.objects.all()
    data= cartData(request)
    items = data['items']
    order = data['order']
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    
    context= {'items':items,'order':order,'cartItems':cartItems,'items':items,'order':order,
    'Shop_list':Shop_list,'mydate':mydate}
    return render (request, "checkout.html",context)


def updateItem(request):
    
    data = json.loads(request.body)
    productId = data['productId']
    action= data['action']
    print ('Action:',action)
    print ('productId:',productId)
    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order , created = Order.objects.get_or_create(customer=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order,product=product)
    
    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)
    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)

def processOrder(request):
    items = data['items']
    order = data['order']
    data = json.loads(request.body)
    transaction_id = datetime.datetime.now().timestamp()

    if request.user.is_authenticated:
        customer = request.user.customer
        order , created = Order.objects.get_or_create(customer=customer, complete=False)
        

    else:
        customer,order = geustOrder(request,data)
        
    total = float(data['form']['total'])
    order.transaction_id = transaction_id
    if total == float(order.get_cart_total):
        order.complete = True
    order.save()
    if order.shipping == True:
        ShippingAddress.objects.create(
            customer=customer,
            order=order,
            address=data['shipping']['address'],
            city=data['shipping']['city'],
            state=data['shipping']['state'],
            zipcode=data['shipping']['zipcode'],
            phone_number=data['shipping']['phone_number'],
        )

    return JsonResponse('Payment submitted..', safe=False)

def ContactView(request):
    Shop_list = Our_Department.objects.all()
    mydate = datetime.datetime.now()
    data= cartData(request)
    items = data['items']
    order = data['order']
    cartItems = data['cartItems']
    form_contact = ContactForm(request.POST)
    if request.method == 'POST':
        if form_contact.is_valid():
            form = ContactForm(request.POST)
            form.save()
            return redirect(reverse('store'))
    else:
        form_contact = ContactForm()
    context={'form_contact':form_contact,
    'mydate':mydate,
    'items':items,
    'order':order,
    'cartItems':cartItems,
    'Shop_list':Shop_list}
    return render(request,'contact-us.html',context)

def About_Us(request):
    Shop_list = Our_Department.objects.all()
    mydate = datetime.datetime.now()
    data= cartData(request)
    items = data['items']
    order = data['order']
    cartItems = data['cartItems']
    context={
    'mydate':mydate,
    'items':items,
    'order':order,
    'cartItems':cartItems,
    'Shop_list':Shop_list}
    return render(request,'about-us.html',context)