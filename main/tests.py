from django.test import TestCase
from .models import Package, Product, Manufacturer, ProductSet
from authentication.models import User
import datetime
# Create your tests here.
class PackageTest(TestCase):
    def setUp(self):
        self.user = User.add_user('cephas','too','admin@admin.com','admin121','A')
        self.user_from_db = User.objects.get_by_natural_key(self.user.email)
        self.manufacturer = Manufacturer.objects.create(user=self.user, name='loasdlo',email='asd@ass.com',location='Nairobi',phone='74521145').save()
        self.product_set = ProductSet(manufacturer =Manufacturer.objects.first(), name='asd', description='asdaa', composition='asdff', image='asddd.jpg').save()
        self.pr1 = Product.objects.create(name='omo', qr_code='awesome.com',sold=False, manufactured=datetime.datetime.utcnow(), product_set=ProductSet.objects.first()).save()
        self.pr2 = Product.objects.create(name='omo', qr_code='awesome.com',sold=False, manufactured=datetime.datetime.utcnow(), product_set=ProductSet.objects.first()).save()
        # self.package = Package.objects.create().save()



    def test_add_user(self):
        self.assertTrue( len(User.objects.all()) > 0 )

    def test_get_by_natural_key(self):
        user = User.objects.get_by_natural_key(self.user.email)
        self.assertTrue( self.user_from_db == self.user)

    def test_edit_user(self):
        user = User.edit_user(self.user.id, 'ken','','admin@admin.com')
        self.assertNotEqual(user.first_name, self.user.first_name)
    
    def test_add_to_package(self):
        package = Package.add_to_package([Product.objects.last(), Product.objects.first()], self.user_from_db)
        self.assertIsNotNone(package)

        
