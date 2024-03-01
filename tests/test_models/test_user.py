from models.base_model import BaseModel
from models.user import User
import unittest
from models import FileStorage


class TestUser(unittest.TestCase):
    def testname(self):
        instance = User()
        instance.first_name = "German"
        key = instance.__class__.__name__ + "." + instance.id
        self.assertEqual(instance.first_name, 'German')
        self.assertEqual(FileStorage._FileStorage__objects[key].first_name, instance.first_name)

    def testemail(self):
        instance = User()
        instance.email = "germanfernando@hotmail.com"
        key = instance.__class__.__name__ + "." + instance.id
        self.assertEqual(instance.email, 'germanfernando@hotmail.com')
        self.assertEqual(FileStorage._FileStorage__objects[key].email, instance.email)
        
    def testpassword(self):
        instance = User()
        instance.password = "holbertoriano"
        key = instance.__class__.__name__ + "." + instance.id
        self.assertEqual(instance.password, 'holbertoriano')
        self.assertEqual(FileStorage._FileStorage__objects[key].password, instance.password)
    
    def testlastname(self):
        instance = User()
        instance.last_name = "Rivero"
        key = instance.__class__.__name__ + "." + instance.id
        self.assertEqual(instance.last_name, 'Rivero')
        self.assertEqual(FileStorage._FileStorage__objects[key].last_name, instance.last_name)
        
    
    if __name__ == '__main__':
        unittest.main()
