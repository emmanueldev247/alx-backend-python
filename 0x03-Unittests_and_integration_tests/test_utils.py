#!/usr/bin/env python3
"""Parameterize a unit test"""

import unittest
from parameterized import parameterized
from unittest.mock import (
    patch,
    Mock,
)
from typing import (
    Mapping,
    Sequence,
    Any,
)
from utils import (
    access_nested_map,
    get_json,
    memoize,
)


class TestAccessNestedMap(unittest.TestCase):
    """class that inherits from unittest.TestCase"""

    @parameterized.expand([
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map: Mapping,
                               path: Sequence, expected: Any):
        """test case for access_nested_map"""
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected)

    @parameterized.expand([
            ({}, ("a",), KeyError),
            ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(self, nested_map: Mapping,
                                         path: Sequence, expected: Any):
        """test case for access_nested_map where KeyError is raised"""
        if expected == KeyError:
            with self.assertRaises(KeyError):
                access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """test class for get_json function"""

    @parameterized.expand([
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False}),
    ])
    @patch("utils.requests.get")
    def test_get_json(self, test_url: str, test_payload: dict, mock_get: Mock):
        """test case for get_json"""

        mock_response = Mock()
        mock_response.json.return_value = test_payload

        mock_get.return_value = mock_response

        result = get_json(test_url)

        self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """test class for memoize function"""

    class TestClass:
        def a_method(self):
            """A sample method returning a fixed value"""
            return 42

        @memoize
        def a_property(self):
            """A memoized property that calls a_method"""
            return self.a_method()

    def test_memoize(self):
        """Test that memoize caches the result after the first call"""
        test_instance = self.TestClass()

        with patch.object(test_instance, 'a_method',
                          return_value=42) as mock_method:
            result1 = test_instance.a_property
            result2 = test_instance.a_property

            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)

            mock_method.assert_called_once()


if __name__ == "__main__":
    unittest.main()
