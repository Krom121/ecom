from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='home'),
    path('contact/', views.contact, name='contact'),
    path('blog/', views.list, name='list'),
    path('shop/', views.product_list, name='product_list'),
]