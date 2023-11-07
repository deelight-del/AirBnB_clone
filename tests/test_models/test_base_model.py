#!/usr/bin/python3
"""Test module for the class BaseModel"""

import unittest
from models.base_model import BaseModel
from datetime import datetime, timedelta
from unittest.mock import patch
from io import StringIO


class TestBaseModel(unittest.TestCase):
    """Class definition of the TestCases for the BaseModel"""
    def setUp(self):
        """Set up method"""
        self.obj1 = BaseModel()
        self.obj2 = BaseModel()

    def test_id(self):
        """Test for the id component"""
        base_obj1 = BaseModel()
        base_obj1.cat = "meow"
        base_obj2 = BaseModel()
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
        self.assertRegex(print_str, r"^\[BaseModel\] \([^)]+\) \{[^}]*\}")

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
        save_dict = self.obj1.to_dict()
        self.assertIsInstance(save_dict, dict)
        self.assertEqual(save_dict["__class__"], "BaseModel")
        self.assertRegex(save_dict["id"], r"^\w+-\w+-\w+-\w+-\w+$")
        self.assertRegex(
                save_dict["created_at"],
                r"^\d{1,4}-([0][1-9]|[1][0-2])-\d\d.+"
                )
        self.assertRegex(
                save_dict["updated_at"],
                r"^\d{1,4}-([0][1-9]|[1][0-2])-\d\d.+"
                )
