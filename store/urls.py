from django.urls import path
from . import views


urlpatterns = [
        #Leave as empty string for base url
	path('', views.Store, name="store"),
	path('shop/all/products/in', views.ShopAllIn, name="ShopAllIn"),
	path('s/', views.search, name="search"),
	path('cart/', views.Cart, name="cart"),
	path('Recommendations/', views.Recommendations, name="Recommendations"),
	path('checkout/', views.Checkout, name="checkout"),
	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),
	path('floop_basic/', views.floop_basic, name="floop_basic"),
	path('shop/category/<str:cats>', views.CategoryView , name='category'),
	path('saleproducts/corner', views.Sale_Viwe , name='Saleproducts'),
	path('bestseller/corner', views.best_seller , name='bestseller'),
	path('offerday/', views.Offer_day , name='offerday'),
	path('customer/display/', views.Customer_sirves , name='customer_sirves'),
	path('post_product/', views.Post_product, name="post_product"),
	path('ContactView/', views.ContactView, name="ContactView"),
	path('About_Us/', views.About_Us, name="About_Us"),
	path('Category_Home/', views.Category_Home, name="Category_Home"),
	path('shop/all/', views.SHopView, name="SHop_View"),
	path('<str:slug>', views.product_deteil,name="product_deteil"),
]