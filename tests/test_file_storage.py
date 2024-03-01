import unittest
import os
from models import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        # Set up a clean state before each test
        FileStorage._FileStorage__objects = {}
    def test_all_method(self):
        # Test the all method
        file_storage = FileStorage()
        all_objects = file_storage.all()

        # Checks
        self.assertIsInstance(all_objects, dict)
        self.assertEqual(all_objects, FileStorage._FileStorage__objects)

    def test_new_method(self):
        # Test the new method
        file_storage = FileStorage()
        obj = BaseModel()
        file_storage.new(obj)

        # Checks
        key = obj.__class__.__name__ + "." + obj.id
        self.assertTrue(key in FileStorage._FileStorage__objects)
        self.assertEqual(FileStorage._FileStorage__objects[key], obj)

    def test_save_and_reload_methods(self):
        # Test the save and reload methods
        file_storage = FileStorage()

        # Add an object to FileStorage
        obj = BaseModel()
        file_storage.new(obj)

        # Save the objects to file
        file_storage.save()

        # Clear objects from FileStorage
        FileStorage._FileStorage__objects = {}

        # Reload the objects from file
        file_storage.reload()

        # Checks
        key = obj.__class__.__name__ + "." + obj.id
        self.assertTrue(key in FileStorage._FileStorage__objects)
        reloaded_obj = FileStorage._FileStorage__objects[key]
        self.assertEqual(reloaded_obj.id, obj.id)
        self.assertEqual(reloaded_obj.created_at, obj.created_at)
        self.assertEqual(reloaded_obj.updated_at, obj.updated_at)

    def test_reload_method_without_file(self):
        # Test the reload method when the file does not exist
        file_path = FileStorage._FileStorage__file_path
        if os.path.exists(file_path):
            os.remove(file_path)

        file_storage = FileStorage()
        file_storage.reload()

        # Checks
        self.assertEqual(FileStorage._FileStorage__objects, {})

    if __name__ == '__main__':
        unittest.main()