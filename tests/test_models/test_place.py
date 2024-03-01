from models.base_model import BaseModel
from models.place import Place
import unittest
from models import FileStorage


class TestPlace(unittest.TestCase):
    def testname(self):
        instance = Place()
        instance.name = "Lezica"
        key = instance.__class__.__name__ + "." + instance.id
        self.assertEqual(instance.name, 'Lezica')
        self.assertEqual(FileStorage._FileStorage__objects[key].name, instance.name)

    if __name__ == '__main__':
        unittest.main()