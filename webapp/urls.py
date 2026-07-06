"""WebC URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [ 


    path('', views.homepage, name="WelcomeHome"),
    path('adminlogin/', views.adminlogin, name="adminlogin"),
    path('adminloginaction/', views.adminloginaction, name="adminloginaction"),
    path('adminhome/', views.adminhome, name="adminhome"),
    path('adminlogout/', views.adminlogout, name="adminlogout"),
    path('viewmanufacturers/', views.viewmanufacturers, name="viewmanufacturers"),
    path('acceptor/', views.acceptor, name="acceptor"),
    
    
    path('userhome/', views.userhome, name="userhome"),
    path('usignupaction/', views.usignupaction, name="usignupaction"),
    path('user/', views.user, name="user"),
    path('userloginaction/', views.userloginaction, name="userloginaction"),
    path('userlogout/', views.userlogout, name="userlogout"),
    path('viewprofile/', views.viewprofilepage, name="viewprofile"),
    
    path('msignupaction/', views.msignupaction, name="msignupaction"),
    path('manufacturer/', views.manufacturer, name="manufacturer"),
    path('mloginaction/', views.mloginaction, name="mloginaction"),
    path('mhome/', views.mhome, name="mhome"),
    path('mlogout/', views.mlogout, name="mlogout"),
    path('adddrug/', views.adddrug, name="adddrug"),
    path('viewdrug/', views.viewdrug, name="viewdrug"),
    path('viewstock/', views.viewstock, name="viewstock"),
    path('addstock/', views.addstock, name="addstock"),
    
    path('psignupaction/', views.psignupaction, name="psignupaction"),
    path('pharmacy/', views.pharmacy, name="pharmacy"),
    path('ploginaction/', views.ploginaction, name="ploginaction"),
    path('plogout/', views.plogout, name="plogout"),
    path('p_home/', views.p_home, name="p_home"),
    path('pviewdrugs/', views.pviewdrugs, name="pviewdrugs"),
    path('addtocart_p/', views.addtocart_p, name="addtocart_p"),
    path('pviewcart/', views.pviewcart, name="pviewcart"),
    path('payment_p/', views.payment_p, name="payment_p"),
    path('pviewstocks/', views.pviewstocks, name="pviewstocks"),
    
    
    path('u_viewdrug/', views.u_viewdrug, name="u_viewdrug"),
    path('addtocart_u/', views.addtocart_u, name="addtocart_p"),
    path('uviewcart/', views.uviewcart, name="uviewcart"),
    path('payment_u/', views.payment_u, name="payment_u"),
    path('view_u/', views.view_u, name="view_u"),
    
    
    
    
    
    


    
    

   
]
