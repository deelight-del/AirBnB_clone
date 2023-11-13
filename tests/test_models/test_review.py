#!/usr/bin/python3
"""Test module for the class Review"""

import unittest
from models.base_model import BaseModel
from models.review import Review
from datetime import datetime, timedelta
from unittest.mock import patch
from io import StringIO
from uuid import uuid4
from models.engine.file_storage import FileStorage
import os


class TestReview(unittest.TestCase):
    """Class definition of the TestCases for the Review"""
    def setUp(self):
        """Set up method"""
        self.obj1 = Review()
        self.obj2 = Review()
        fs = FileStorage()
        fs.reset()
        if os.path.exists("file.json"):
            os.remove("file.json")

    def tearDown(self):
        """Tear down method to be used after each test_method"""
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_id(self):
        """Test for the id component"""
        base_obj1 = Review()
        base_obj1.cat = "meow"
        base_obj2 = Review()
        self.assertIsInstance(base_obj1.id, str)
        self.assertEqual(base_obj1.cat, "meow")
        self.assertNotEqual(base_obj1.id, base_obj2.id)
        self.assertGreaterEqual(len(base_obj1.id), 32)
        self.assertGreaterEqual(len(base_obj2.id), 32)
        self.assertRegex(base_obj1.id, r"^\w+-\w+-\w+-\w+-\w+$")

    def test_created_updated_attr(self):
        """Test for created_at and updated_at"""
        self.assertIsInstance(self.obj1.created_at, datetime)
        self.assertIsInstance(self.obj1.updated_at, datetime)
        expected_diff = timedelta(seconds=10)
        actual_diff = self.obj1.created_at - datetime.now()
        self.assertLess(actual_diff, expected_diff)
        expected_diff = timedelta(seconds=10)
        actual_diff = self.obj1.updated_at - datetime.now()
        self.assertLess(actual_diff, expected_diff)

    def test_print_str(self):
        """Test for the printing capacity"""
        print_str = self.obj1.__str__()
        self.assertGreater(len(print_str), 35)
        self.assertRegex(print_str, r"^\[Review\] \([^)]+\) \{[^}]*\}")

    def test_save(self):
        """ Testing for the save method of the object """
        former_updated_at = self.obj1.updated_at
        former_created_at = self.obj1.created_at
        self.assertEqual(former_updated_at, self.obj1.updated_at)
        self.assertEqual(former_created_at, self.obj1.created_at)
        self.obj1.save()
        self.assertNotEqual(former_updated_at, self.obj1.updated_at)
        self.assertEqual(former_created_at, self.obj1.created_at)

    def test_to_dict(self):
        """ Testing the to_dict serialization method """
        self.obj1.first_name = "foo"
        self.obj1.last_name = "bar"
        self.obj1.email = "foobar@hbtn.com"
        self.obj1.password = "root"
        save_dict = self.obj1.to_dict()
        self.assertIsInstance(save_dict, dict)
        self.assertEqual(save_dict["__class__"], "Review")
        self.assertRegex(save_dict["id"], r"^\w+-\w+-\w+-\w+-\w+$")
        self.assertRegex(
                save_dict["created_at"],
                r"^\d{1,4}-([0][1-9]|[1][0-2])-\d\d.+"
                )
        self.assertRegex(
                save_dict["updated_at"],
                r"^\d{1,4}-([0][1-9]|[1][0-2])-\d\d.+"
                )
        self.assertEqual(save_dict["first_name"], "foo")
        self.assertEqual(save_dict["last_name"], "bar")
        self.assertEqual(save_dict["email"], "foobar@hbtn.com")
        self.assertEqual(save_dict["password"], "root")
        save_dict = self.obj2.to_dict()
        self.assertIsNone(save_dict.get("first_name", None))
        self.assertIsNone(save_dict.get("last_name", None))
        self.assertIsNone(save_dict.get("email", None))
        self.assertIsNone(save_dict.get("password", None))

    def test_init(self):
        """ This method will test the init method of the Review class """
        attrs_dict = {"id": str(uuid4())}
        obj = Review(**attrs_dict)
        id_attr = getattr(obj, "id", None)
        created_attr = getattr(obj, "created_at", None)
        updated_attr = getattr(obj, "updated_at", None)
        class_name_attr = getattr(obj, "__class__", None)
        self.assertEqual(id_attr, attrs_dict["id"])
        self.assertIsNone(created_attr)
        self.assertIsNone(updated_attr)
        self.assertNotEqual(class_name_attr, "Review")
        # Vary the created_at.
        obj_dict = self.obj1.to_dict()
        attrs_dict = {"created_at": obj_dict["created_at"]}
        obj = Review(**attrs_dict)
        id_attr = getattr(obj, "id", None)
        created_attr = getattr(obj, "created_at", None)
        updated_attr = getattr(obj, "updated_at", None)
        self.assertIsNone(id_attr)
        self.assertIsInstance(created_attr, datetime)
        self.assertIsNone(updated_attr)
        # Vary the updated_at.
        attrs_dict = {"updated_at": obj_dict["updated_at"]}
        obj = Review(**attrs_dict)
        id_attr = getattr(obj, "id", None)
        created_attr = getattr(obj, "created_at", None)
        updated_attr = getattr(obj, "updated_at", None)
        self.assertIsNone(id_attr)
        self.assertIsInstance(updated_attr, datetime)
        self.assertIsNone(created_attr)
        # Vary the updated_at.
        attrs_dict = {
                "updated_at": obj_dict["updated_at"],
                "created_at": obj_dict["created_at"]
                }
        obj = Review(**attrs_dict)
        id_attr = getattr(obj, "id", None)
        created_attr = getattr(obj, "created_at", None)
        updated_attr = getattr(obj, "updated_at", None)
        self.assertIsNone(id_attr)
        self.assertIsInstance(updated_attr, datetime)
        self.assertIsInstance(created_attr, datetime)
        # Test, when all of the dictionary is used to initialize an object.
        obj = Review(**obj_dict)
        id_attr = getattr(obj, "id", None)
        created_attr = getattr(obj, "created_at", None)
        updated_attr = getattr(obj, "updated_at", None)
        class_name_attr = getattr(obj, "__class__", None)
        self.assertEqual(id_attr, obj_dict["id"])
        self.assertIsInstance(updated_attr, datetime)
        self.assertIsInstance(created_attr, datetime)
        self.assertNotEqual(class_name_attr, "Review")
        # Initialize with nothing.
        obj2_dict = self.obj2.to_dict()
        created_attr = getattr(obj, "created_at", None)
        updated_attr = getattr(obj, "updated_at", None)
        class_name_attr = getattr(obj, "__class__", None)
        self.assertNotEqual(obj2_dict["id"], obj_dict["id"])
        self.assertIsInstance(updated_attr, datetime)
        self.assertIsInstance(created_attr, datetime)
        self.assertNotEqual(class_name_attr, "Review")

    def test_save_reload(self):
        """The method that tests for the save and reload"""
        fs = FileStorage()
        obj1 = Review()  # This will use the save method.
        obj2 = Review()
        obj2.save()
        fs.reset()
        self.assertDictEqual(fs.all(), {})
        fs.reload()
        expected_dict = fs.all()
        expected_keys = list(expected_dict.keys())
        expected_vals = list(expected_dict.values())
        self.assertIsInstance(expected_dict, dict)
        self.assertEqual(len(expected_keys), 2)
        self.assertRegex(
                expected_keys[0],
                r"^Review\.\w+-\w+-\w+-\w+-\w+$"
                )
        self.assertIsInstance(expected_vals[0], Review)

    def test_new_attributes(self):
        """Method to test for new attributes"""
        self.assertEqual(self.obj1.place_id, "")
        self.assertEqual(self.obj1.user_id, "")
        self.assertEqual(self.obj1.text, "")
        # Test type/instance of each attr.
        self.obj1.place_id = "foo"
        self.assertEqual(self.obj1.place_id, "foo")
        local_dict = {"place_id": "foo"}
        local_obj = Review(**local_dict)
        self.assertEqual(local_obj.place_id, "foo")
