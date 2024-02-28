import json
import os


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        with open(FileStorage.__file_path, 'w') as f:
            serialized_objects = {}

            for key, value in FileStorage.__objects.items():
                dict_object = value.to_dict()

                serialized_objects[key] = dict_object

            json.dump(serialized_objects, f)

    def reload(self):
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as f:
                objs = json.load(f)

            for obj in objs.values():
                class_name = obj['__class__']

                actual_class = eval(class_name)

                deserialized_obj = actual_class(**obj)

                self.new(deserialized_obj)
