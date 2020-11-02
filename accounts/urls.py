from django.urls import path
from . import views
from accounts.views import PasswordsChangeView,EditProfilePageView,ViweProfilePage



urlpatterns = [
	path('register/',views.RegisterView,name='register'),
	
	path('Conditions_of_Use/',views.Conditions_of_Use,name='ConditionsofUse'),
	path('Covid/',views.Covid,name='Covid'),
	path('GetProductHelp/',views.GetProductHelp,name='GetProductHelp'),
	path('Privacy_Notice/',views.Privcy,name='Privacy_Notice'),
	# path('profile', views.ProfileViwe,name='profile'),
	path('change_password/', PasswordsChangeView.as_view(template_name='registration/change_password.html'),name='change_password'),
	path('<int:pk>/profile/', ViweProfilePage.as_view(),name='user_profile_page'),
	path('<int:pk>/edit_profile_page/', EditProfilePageView.as_view(),name='edit_profile_page'),
]