from django.contrib import admin
from django.urls import path
from Home import views 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.indexHome,name='indexHome'),
    path('showHome/',views.showHome,name='showHome'),
    path('detailsHome/<int:id>/',views.detailsHome,name='detailsHome'),
    path('registerHome',views.registerHome,name='registerHome'),
    path('loginHome',views.loginHome,name='loginHome'),
    path('logoutHome',views.logoutHome,name='logoutHome'),
    path('checkoutHome/',views.checkoutHome,name='checkoutHome'),
    path('add_to_cartHome/<int:id>/',views.add_to_cartHome,name='add_to_cartHome'),
    

]
