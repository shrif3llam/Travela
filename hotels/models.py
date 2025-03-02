from django.db import models
# Create your models here.
class Hotel(models.Model):
    name = models.CharField(max_length=255)  # اسم الفندق
    description = models.TextField()  # وصف الفندق
    price = models.DecimalField(max_digits=10, decimal_places=2)  # السعر
    rooms = models.IntegerField()  # عدد الغرف
    bathrooms = models.IntegerField(default=1)  # عدد الحمامات
    wifi = models.BooleanField(default=False)  # هل فيه واي فاي؟
    image = models.ImageField(upload_to='hotels/', blank=True, null=True)  # صورة الفندق
    city = models.CharField(max_length=100,default='Cairo')  # اسم المحافظة
    #created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

