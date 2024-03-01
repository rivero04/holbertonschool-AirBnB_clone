from models.base_model import BaseModel
from models.user import User
import unittest
from models import FileStorage


class TestState(unittest.TestCase):
    def testname(self):
        instance = User()
        instance.first_name = "German"
        key = instance.__class__.__name__ + "." + instance.id
        self.assertEqual(instance.first_name, 'German')
        self.assertEqual(FileStorage._FileStorage__objects[key].first_name, instance.first_name)

    if __name__ == '__main__':
        unittest.main()