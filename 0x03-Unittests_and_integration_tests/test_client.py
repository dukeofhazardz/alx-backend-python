#!/usr/bin/env python3
""" Unittests for Clients """

from parameterized import parameterized
from client import GithubOrgClient
from unittest.mock import patch, Mock
import unittest


class TestGithubOrgClient(unittest.TestCase):
    """ A Test class that tests the GithubOrgClient Class """
    @parameterized.expand([
        ("google"),
        ("abc"),
    ])
    @patch('client.get_json')
    def test_org(self, test_org, get_mock):
        """ Test the org method of the GithubOrgClient Class """
        mock_response = Mock(spec=dict)
        get_mock.return_value = mock_response

        result = GithubOrgClient(test_org)
        self.assertIsInstance(result.org, dict)
        get_mock.assert_called_once_with(GithubOrgClient.ORG_URL.
                                         format(org=test_org))
