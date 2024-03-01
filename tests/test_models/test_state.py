from models.base_model import BaseModel
from models.state import State
import unittest
from models import FileStorage
""" test for State """

class TestState(unittest.TestCase):
    def testname(self):
        #test state name
        instance = State()
        instance.name = "Orlando"
        key = instance.__class__.__name__ + "." + instance.id
        self.assertEqual(instance.name, 'Orlando')
        self.assertEqual(FileStorage._FileStorage__objects[key].name, instance.name)

    if __name__ == '__main__':
        unittest.main()