from django.urls import path
from . import views


urlpatterns = [
            path('',views.home,name='home'),

    path('man/',views.man,name='man'),
        path('woman/',views.woman,name='woman'),
        path('child/',views.child,name='child'),

        path('log/',views.log,name='log'),

        path('about/<int:id>',views.about,name='about'),
    path('push/<int:id>', views.push, name='push'),
        path('payaple/', views.payaple, name='payaple'),


        path('payment_success/', views.payment_success, name='payment_success'),


]