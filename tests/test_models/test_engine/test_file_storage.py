#!/usr/bin/python3
"""This module contain the testing for testing the file_storage
module, particularly the FileStorage class"""
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.engine.file_storage import FileStorage
import unittest
import os
import json


class TestFileStorage(unittest.TestCase):
    """The designed class for testing FileStorage"""
    def setUp(self):
        """The set up method for taking care of set up stuff"""
        fs = FileStorage()
        fs.reset()
        if os.path.exists("file.json"):
            os.remove("file.json")

    def tearDown(self):
        """Tear down method to be used after each test_method"""
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_all_new(self):
        """The method to test the returned dictionary object"""
        fs = FileStorage()
        self.assertDictEqual(fs.all(), {})
        obj1 = BaseModel()  # This will use the save method.
        obj2 = BaseModel()
        obj3 = User()
        obj4 = State()
        obj5 = City()
        obj6 = Amenity()
        obj7 = Place()
        obj8 = Review()
        expected_dict = fs.all()
        expected_keys = list(expected_dict.keys())
        expected_vals = list(expected_dict.values())
        self.assertIsInstance(expected_dict, dict)
        self.assertEqual(len(expected_keys), 8)
        pattern = (
                r"^(BaseModel|User|State|City|Amenity|Place|Review)"
                r"\.\w+-\w+-\w+-\w+-\w+$"
                )
        self.assertRegex(
                expected_keys[0],
                pattern
                )
        pattern = (
                r"^(BaseModel|User|State|City|Amenity|Place|Review)"
                r"\.\w+-\w+-\w+-\w+-\w+$"
                )
        self.assertRegex(
                expected_keys[1],
                pattern
                )
        pattern = (
                r"^(BaseModel|User|State|City|Amenity|Place|Review)"
                r"\.\w+-\w+-\w+-\w+-\w+$"
                )
        self.assertRegex(
                expected_keys[2],
                pattern
                )
        pattern = (
                r"^(BaseModel|User|State|City|Amenity|Place|Review)"
                r"\.\w+-\w+-\w+-\w+-\w+$"
                )
        self.assertRegex(
                expected_keys[3],
                pattern
                )
        pattern = (
                r"^(BaseModel|User|State|City|Amenity|Place|Review)"
                r"\.\w+-\w+-\w+-\w+-\w+$"
                )
        self.assertRegex(
                expected_keys[4],
                pattern
                )
        pattern = (
                r"^(BaseModel|User|State|City|Amenity|Place|Review)"
                r"\.\w+-\w+-\w+-\w+-\w+$"
                )
        self.assertRegex(
                expected_keys[5],
                pattern
                )
        pattern = (
                r"^(BaseModel|User|State|City|Amenity|Place|Review)"
                r"\.\w+-\w+-\w+-\w+-\w+$"
                )
        self.assertRegex(
                expected_keys[6],
                pattern
                )
        pattern = (
                r"^(BaseModel|User|State|City|Amenity|Place|Review)"
                r"\.\w+-\w+-\w+-\w+-\w+$"
                )
        self.assertRegex(
                expected_keys[7],
                pattern
                )
        self.assertIsInstance(expected_vals[0], BaseModel)
        self.assertIsInstance(expected_vals[0], BaseModel)
        self.assertIsInstance(expected_vals[0], BaseModel)
        self.assertIsInstance(expected_vals[0], BaseModel)
        self.assertIsInstance(expected_vals[0], BaseModel)
        self.assertIsInstance(expected_vals[0], BaseModel)
        self.assertIsInstance(expected_vals[0], BaseModel)
        self.assertIsInstance(expected_vals[0], BaseModel)
        self.assertIsInstance(expected_vals[0], BaseModel)
        """Will the length change upon adding a new instance.
        First check for adding an already existing instance and then
        add a new instance"""
        obj3_no_change = BaseModel(**(obj2.to_dict()))
        expected_dict = fs.all()
        expected_keys = list(expected_dict.keys())
        self.assertEqual(len(expected_keys), 8)
        obj3_change = BaseModel()
        expected_dict = fs.all()
        expected_keys = list(expected_dict.keys())
        self.assertEqual(len(expected_keys), 9)
        given_key = f"BaseModel.{obj3_change.id}"
        self.assertIsNotNone(expected_dict[given_key])

    def test_save(self):
        fs = FileStorage()
        fs.reset()
        fs.save()
        with open("file.json", "r", encoding="utf-8") as f:
            json_dict = json.load(f)
            self.assertEqual(dict(), json_dict)
        obj1 = BaseModel()  # This will use the save method.
        obj2 = BaseModel()
        fs.save()
        with open("file.json", "r", encoding="utf-8") as f:
            json_dict = json.load(f)
        expected_keys = list(json_dict.keys())
        expected_vals = list(json_dict.values())
        self.assertIsInstance(json_dict, dict)
        self.assertEqual(len(expected_keys), 2)
        self.assertRegex(
                expected_keys[0],
                r"^BaseModel\.\w+-\w+-\w+-\w+-\w+$"
                )
        self.assertIsInstance(expected_vals[0], dict)
        value_dict = expected_vals[0]
        self.assertEqual(value_dict["__class__"], "BaseModel")
        self.assertRegex(value_dict["id"], r"^\w+-\w+-\w+-\w+-\w+$")
        self.assertRegex(
                value_dict["created_at"],
                r"^\d{1,4}-([0][1-9]|[1][0-2])-\d\d.+"
                )
        self.assertRegex(
                value_dict["updated_at"],
                r"^\d{1,4}-([0][1-9]|[1][0-2])-\d\d.+"
                )

    def test_reload(self):
        fs = FileStorage()
        fs.reload()
        self.assertDictEqual(fs.all(), {})
        obj1 = BaseModel()  # This will use the save method.
        obj2 = BaseModel()
        fs.save()
        fs.reset()
        self.assertDictEqual(fs.all(), {})
        fs.reload()
        expected_dict = fs.all()
        expected_keys = list(expected_dict.keys())
        expected_vals = list(expected_dict.values())
        self.assertIsInstance(expected_dict, dict)
        self.assertEqual(len(expected_keys), 2)
        pattern = (
                r"^(BaseModel|User|State|City|Amenity|Place|Review)"
                r"\.\w+-\w+-\w+-\w+-\w+$"
                )
        self.assertRegex(
                expected_keys[0],
                pattern
                )
