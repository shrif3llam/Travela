from django.db import models
from django.utils.timezone import now

# Create your models here.

CITY = (
    ('Cairo','Cairo'),
    ('Alexandria','Alexandria'),
    ('Aswan','Aswan'),
    ('Giza','Giza'),
    ('Hurgada','Hurgada'),
    ('Luxor','Luxor'),
    ('Sharm El-Shakh','Sharm El-Shakh'),
)
Rooms=(
    (1,1),
    (2,2),
    (3,3),
    (4,4),
    (5,5),
    (6,6),
)
Bath_Rooms=(
    (1,1),
    (2,2),
    (3,3),
)


class Hotel(models.Model):
    name = models.CharField(max_length=255)  # اسم الفندق
    description = models.TextField(max_length=1000)  # وصف الفندق
    price = models.DecimalField(max_digits=10, decimal_places=2)  # السعر
    beds = models.IntegerField(choices=Rooms,default=1)  # عدد الغرف
    baths = models.IntegerField(choices=Bath_Rooms,default=1)  # عدد الحمامات
    wifi = models.BooleanField(default=False)  # هل فيه واي فاي؟
    rating = models.IntegerField(default=5)
    image = models.ImageField(upload_to='hotels/images/', blank=True, null=True)  # صورة الفندق
    city = models.CharField(max_length=100,default='Cairo',choices=CITY)  # اسم المحافظة
    created_at = models.DateTimeField(auto_now=True)
    category=models.ForeignKey('Category',on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Category(models.Model):
    name=models.CharField(max_length=25)
    def __str__(self):
        return self.name