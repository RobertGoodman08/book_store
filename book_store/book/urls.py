from django.urls import path
from book.views import base, get_single, get_category, register,user_login,user_logout, logout
from . import views

urlpatterns = [
    path('', base, name='base'),
    path('<int:slug>/', views.get_single, name='single'),
    path('category/<int:category_id>/', get_category, name='category'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('search/', views.get_search, name='search'),
]
