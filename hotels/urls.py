from django.urls import path , include
from . import views
from .views import hotel_detail
urlpatterns = [
    path('',views.index,name='index'),
    path('hotels',views.hotel_list),
    path('hotels/<int:id>/',views.hotel_detail),
]