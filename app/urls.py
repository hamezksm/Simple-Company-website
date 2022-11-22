from app import views
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

#Create your urls here.

urlpatterns = [
    path('', views.home, name=''),
    path('about/',views.about, name='about'),
    path('products/',views.products, name='products'),
    path('contacts/', views.contacts, name='contacts'),
    path('custdets/', views.custdets, name='custdets'),
]

# re-edit the form_view to a precise url
# set a home page url
