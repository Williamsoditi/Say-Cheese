from ast import Load
from django.test import TestCase
from .models import Pictures, Category, Location

# Create your tests here.
class LocationTestClass(TestCase):
    def setUp(self):
        self.strathmore = Location(locate='Strathmore')
    
    def test_location_instance(self):
        self.assertTrue(isinstance(self.strathmore,Location))

    def test_save_location(self):
        self.strathmore.save_location()
        places = Location.objects.all()
        self.assertTrue(len(places)>0)
    
    def test_delete_location(self):
        self.strathmore.save_location()
        places = Location.objects.all()
        self.assertEqual(len(places),1)
        self.strathmore.delete_location()
        places = Location.objects.all()
        self.assertEqual(len(places),0)

    def test_display_locations(self):
        self.strathmore.save_location()
        self.assertEqual(len(Location.display_all_locations()),1)

    def test_update_location(self):
        self.strathmore.save_location()
        self.strathmore.update_location(self.strathmore.id,'alice')
        update = Location.objects.get(locate = 'alice')
        self.assertTrue(update.locate, 'alice')



class CategoryTestClass(TestCase):
    def setUp(self):
        self.sports = Category(name = 'sports')
    
    def test_save_category(self):
        self.sports.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories)>0)

    def test_delete_category(self):
        self.sports.save_category()
        categories= Category.objects.all()
        self.assertEqual(len(categories),1)
        self.sports.delete_category()
        categories=Category.objects.all()
        self.assertEqual(len(categories),0)

    def test_update_category(self):
        self.sports.save_category()
        self.sports.update_category(self.sports.id,'alice')
        update = Category.objects.get(name = "alice")
        self.assertTrue(update.name, 'alice')

    def test_display_categories(self):
        self.sports.save_category()
        self.assertEqual(len(Category.display_all_categories()),1)