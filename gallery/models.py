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
    locate = models.CharField(max_length=50)

    def __str__(self):
        return self.locate
        
    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    @classmethod
    def update_location(cls,id,name):
        cls.objects.filter(id = id).update(locate = name)

    @classmethod
    def display_all_locations(cls):
        return cls.objects.all()

class Pictures(models.Model):
    image = CloudinaryField('image')
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=2000)
    category = models.ForeignKey('Category',on_delete=models.CASCADE, null=True)
    location = models.ForeignKey('Location',on_delete=models.CASCADE, null=True)
    post_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

    @classmethod
    def get_all_pictures(cls):
        pictures = Pictures.objects.all()
        return pictures

    @classmethod
    def get_pic_by_id(cls,id):
        pic = cls.objects.get(id=id)
        return pic

    @classmethod
    def search_by_category(cls,search_term):
        gallery = cls.objects.filter(category__name__icontains=search_term)
        return gallery

    @classmethod
    def filter_by_location(cls, location):
        pictures = Pictures.objects.filter(location__name=location)
        return pictures

    @classmethod
    def display_all_images(cls):
        return cls.objects.all()

    def save_picture(self):
        self.save()

    def update_picture(self,name,description,category):
        self.name = name,
        self.description = description,
        self.category = category
        self.save()

    def get_picture_by_id(cls,id):
        pic = Pictures.objects.get(id=id)
        return pic

    class Meta:
        ordering = ['-post_date']