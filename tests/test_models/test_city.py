from models.base_model import BaseModel
from models.city import City
import unittest
from models import FileStorage


class TestCity(unittest.TestCase):
    def testname(self):
        instance = City()
        instance.name = "Montevideo"
        key = instance.__class__.__name__ + "." + instance.id
        self.assertEqual(instance.name, 'Montevideo')
        self.assertEqual(FileStorage._FileStorage__objects[key].name, instance.name)

    if __name__ == '__main__':
        unittest.main()