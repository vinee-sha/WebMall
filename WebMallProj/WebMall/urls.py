from django.urls import path
from . import views

urlpatterns = [
    path('', views.login),
    path('Login/', views.login, name = 'login'),
    path('Register/', views.register, name = 'register'),
    path('ForgotPassword/', views.forgotPass, name = 'forgotPass'),
    path('Shop/', views.index, name = 'index'),
    path('Boys/', views.boys, name = 'boys'),
    path('BoysView/', views.boyView, name = 'boyView'),
    path('Girls/', views.girls, name = 'girls'),
    path('GirlsView/', views.girlView, name = 'girlView'),
    path('Men/', views.men, name = 'men'),
    path('MenView/', views.menView, name = 'menView'),
    path('Women/', views.women, name = 'women'),
    path('WomenView/', views.womenView, name = 'womenView'),
    path('Checkout/', views.checkout, name = 'checkout'),
    path('Contact/', views.contact, name = 'contact'),
    path('FAQ/', views.faq, name = 'faq'),
    path('Payment/', views.payment, name = 'payment'),
]