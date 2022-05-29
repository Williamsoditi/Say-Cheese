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