from django.urls import path

from.import views

urlpatterns = [
    path('',views.home, name='home'),
    path('accomodation',views.accomodation,name='accomodation'),
    path('hotelDetails', views.hotelDetails,name='hotelDetails'),
    path('hotellist',views.hotellist,name='hotellist')
]
