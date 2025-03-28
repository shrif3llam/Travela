from django.shortcuts import render,get_object_or_404
from .models import Hotel
# Create your views here.
def hotel_list(request):
    hotel_list=Hotel.objects.all()
    context={'hotels':hotel_list}
    return render(request,'hotels/hotel_list.html',context)

def index(request):
    rooms = Hotel.objects.all()
    context = {'rooms': rooms}
    return render(request,'hotels/index.html',context)

def hotel_detail(request, id):
    hotel_detail=Hotel.objects.get(id=id)
    context={'hotel':hotel_detail}
    return render(request,'hotels/hotel_detail.html',context)