from models.base_model import BaseModel
from models.review import Review
import unittest
from models import FileStorage


class TestReview(unittest.TestCase):
    def testname(self):
        instance = Review()
        instance.text = "Beautiful Place"
        key = instance.__class__.__name__ + "." + instance.id
        self.assertEqual(instance.text, 'Beautiful Place')
        self.assertEqual(FileStorage._FileStorage__objects[key].text, instance.text)

    if __name__ == '__main__':
        unittest.main()
