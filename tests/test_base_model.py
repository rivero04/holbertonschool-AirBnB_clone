import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """ Run all the tests for the base_model """

    def test_init_with_args(self):
        # Test initialization with arguments
        kwargs = {
            'created_at': '2022-01-01T12:00:00.000000',
            'updated_at': '2022-01-01T14:00:00.000000',
            'other_key': 'other_value'
        }
        instance = BaseModel(**kwargs)

        # Checks
        self.assertEqual(instance.created_at, datetime(2022, 1, 1, 12, 0, 0))
        self.assertEqual(instance.updated_at, datetime(2022, 1, 1, 14, 0, 0))
        self.assertEqual(instance.other_key, 'other_value')

    def test_init_without_args(self):
        # Test initialization without arguments
        instance = BaseModel()

        # Checks
        self.assertTrue(hasattr(instance, 'id'))
        self.assertTrue(hasattr(instance, 'created_at'))
        self.assertTrue(hasattr(instance, 'updated_at'))
        self.assertTrue(isinstance(instance.id, str))
        self.assertTrue(isinstance(instance.created_at, datetime))
        self.assertTrue(isinstance(instance.updated_at, datetime))

    def test_str_method(self):
        # Test the __str__ method
        instance = BaseModel()
        instance_str = str(instance)

        # Checks
        self.assertIn(instance.__class__.__name__, instance_str)
        self.assertIn(instance.id, instance_str)
        self.assertIn(str(instance.__dict__), instance_str)

    def test_save_method(self):
        # Test the save method
        instance = BaseModel()
        initial_updated_at = instance.updated_at
        instance.save()

        # Checks
        self.assertNotEqual(initial_updated_at, instance.updated_at)

    def test_to_dict_method(self):
        # Test the to_dict method
        instance = BaseModel()
        instance_dict = instance.to_dict()

        # Checks
        self.assertTrue('__class__' in instance_dict)
        self.assertTrue('created_at' in instance_dict)
        self.assertTrue('updated_at' in instance_dict)
        self.assertEqual(instance_dict['__class__'], instance.__class__.__name__)
        self.assertEqual(instance_dict['created_at'], instance.created_at.isoformat())
        self.assertEqual(instance_dict['updated_at'], instance.updated_at.isoformat())

if __name__ == '__main__':
    unittest.main()