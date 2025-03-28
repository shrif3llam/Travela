from django.urls import path , include
from . import views
from .views import hotel_detail
urlpatterns = [
    #Header
    path('',views.index,name='home'),
    path('about',views.index,name='about'),
    path('booking',views.Booking,name='booking'),
    path('search',views.index,name='search'),
    path('travel',views.Travel,name='travel'),
    path('contact',views.Contact,name='contact'),
    path('pages',views.index,name='pages'),
    path('hotels',views.hotel_list),
    path('hotels/<int:id>/',views.hotel_detail),
    
    #Govers
    path('govers/alex',views.Alex,name='alex'),
    path('govers/cairo',views.Cairo,name='cairo'),
]