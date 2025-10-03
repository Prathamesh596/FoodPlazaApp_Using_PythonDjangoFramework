from django.urls import path
from . import views

urlpatterns=[

    (path('displayfoodform',views.displayfoodform,name='displayfoodform')),
    (path('addfood',views.addfood,name='addfood')),
    (path('showfood',views.showfood,name='showfood')),
    (path('updatefoodform',views.updatefoodform,name='updatefoodform')),
    (path('getfood/updatefood',views.updatefood,name='updatefood')),
    (path('getfood/<int:foodId>',views.getfood,name='getfood')),
    (path('deletefood/<int:foodId>',views.deletefood,name='deletefood')),
    
    
    (path('displaycustform',views.displaycustomerform,name='displaycustform')),
    (path('addcust',views.addcust,name='addcust')),
    (path('showcust',views.showcust,name='showcust')),
    (path('updatecustform',views.updatecustform,name='updatecustform')),
    (path('getcust/updatecust',views.updatecust,name='updatecust')),
    (path('getcust',views.getcust,name='getcust')),
    (path('deletecust/<str:custEmail>',views.deletecust,name='deletecust')),

    (path('displaycart/<int:foodId>',views.displaycart,name='displaycart')),
    (path('displaycart/savecart',views.addcart,name='addcart')),
    (path('displaycart/savecart',views.addcart1,name='addcart1')),
    (path('showcart',views.showcart,name='showcart')),
    (path('deletecart/<int:cartId>',views.deletecart,name='deletecart')),


    (path('login',views.Login,name='Login')),
    (path('displayLogin',views.displayLoginForm,name='displayLoginForm')),

    (path('viewpass',views.updatepass,name='updatepass')), 
    (path('updatepass',views.updatepassword,name='updatepassword')) ,

    (path('index',views.displayIndex,name='displayIndex')) ,        
    (path('logout',views.logout,name='logout')) ,

    (path('placeOrder',views.placeOrder,name='placeorder')),

    (path('clearcart',views.clearCart,name='clearCart')),
     (path('myorders',views.showOrders,name='showOrders')),

      
]