from django.shortcuts import render,get_object_or_404
from .models import Hotel
# Create your views here.

#Header

def index(request):
    rooms = Hotel.objects.all()
    context = {'rooms': rooms}
    return render(request,'hotels/index.html',context)

def Contact(request):
    return render(request,'hotels/contact.html')

def Travel(request):
    return render(request,'hotels/Travel.html')

def Booking(request):
    rooms = Hotel.objects.all()
    context = {'rooms': rooms}
    return render(request,'hotels/booking.html',context)

def hotel_list(request):
    hotel_list=Hotel.objects.all()
    context={'hotels':hotel_list}
    return render(request,'hotels/hotel_list.html',context)
def hotel_detail(request, id):
    hotel_detail=Hotel.objects.get(id=id)
    context={'hotel':hotel_detail}
    return render(request,'hotels/hotel_detail.html',context)




#Govers

def Alex(request):
    rooms = Hotel.objects.all()
    context = {'rooms': rooms}
    return render(request, 'hotels/Govers/alex.html', context)

def Cairo(request):
    rooms = Hotel.objects.all()
    context = {'rooms': rooms}
    return render(request, 'hotels/Govers/cairo.html', context)