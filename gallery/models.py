from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    @classmethod
    def update_category(cls,id,name):
        cls.objects.filter(id = id).update(name = name)

    @classmethod
    def display_all_categories(cls):
        return cls.objects.all()

class Location(models.Model):
    loc = models.CharField(max_length=50)

    def __str__(self):
        return self.loc
        
    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    @classmethod
    def update_location(cls,id,name):
        cls.objects.filter(id = id).update(loc = name)

    @classmethod
    def display_all_locations(cls):
        return cls.objects.all()


