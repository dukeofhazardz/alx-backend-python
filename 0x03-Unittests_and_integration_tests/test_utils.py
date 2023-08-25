#!/usr/bin/env python3
""" Unittests for Utils """

from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch, Mock
import unittest


class TestAccessNestedMap(unittest.TestCase):
    """ A class that tests the access_nested_map function """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """ A method that tests the access_nested_map function """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """ A method that tests the access_nested_map function exception """
        self.assertRaises(expected, access_nested_map, nested_map, path)


class TestGetJson(unittest.TestCase):
    """ A class that tests the get_json function """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """ A method that tests the get_json function """
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        result = get_json(test_url)
        self.assertEqual(result, test_payload)
        mock_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """ A class that tests the memoize function """
    def test_memoize(self):
        """ A method that tests the memozie function """
        class TestClass:
            """ A TestClass class """
            def a_method(self):
                """ A method that returns 42 """
                return 42

            @memoize
            def a_property(self):
                """ A method that memoizes the a_method method """
                return self.a_method()

        test = TestClass()
        with patch.object(test, 'a_method') as mock_a_property:
            mock_a_property.return_value = 42
            result1 = test.a_property
            result2 = test.a_property

            mock_a_property.assert_called_once()
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)
