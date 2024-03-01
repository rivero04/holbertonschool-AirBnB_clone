from models.base_model import BaseModel
from models.amenity import Amenity
import unittest

class TestAmenity(unittest.TestCase):
    def testname(self):
        instance = Amenity()
        instance.name = "Pedro"

        self.assertEqual(instance.name, 'Pedro')

    if __name__ == '__main__':
        unittest.main()