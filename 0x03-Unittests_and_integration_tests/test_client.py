#!/usr/bin/env python3
""" Unittests for Clients """

from parameterized import parameterized
from client import GithubOrgClient
from unittest.mock import patch, Mock, PropertyMock
import unittest


class TestGithubOrgClient(unittest.TestCase):
    """ A Test class that tests the GithubOrgClient Class """
    @parameterized.expand([
        ("google"),
        ("abc"),
    ])
    @patch('client.get_json')
    def test_org(self, test_org, get_mock):
        """ Tests the org method of the GithubOrgClient Class """
        mock_response = Mock(spec=dict)
        get_mock.return_value = mock_response

        result = GithubOrgClient(test_org)
        self.assertIsInstance(result.org, dict)
        get_mock.assert_called_once_with(GithubOrgClient.ORG_URL.
                                         format(org=test_org))

    def test_public_repos_url(self):
        """ Tests the _public_repos_url method """
        mock_payload = {"repos_url": "https://api.github.com/orgs/apple/repos"}
        with patch.object(GithubOrgClient, 'org', new_callable=PropertyMock,
                          return_value=mock_payload):
            apple = GithubOrgClient("apple")._public_repos_url

            self.assertEqual(apple, mock_payload["repos_url"])

    @patch('client.get_json')
    def test_public_repos(self, get_mock):
        """ Tests the public_repos method of GithubOrgClient Class """
        mock_payload = [
            {"name": "repo1", "license": {"key": "MIT"}},
            {"name": "repo2", "license": None},
            {"name": "repo3", "license": {"key": "Apache-2.0"}},
        ]
        get_mock.return_value = mock_payload

        with patch.object(GithubOrgClient, '_public_repos_url',
                          return_value=200):
            google = GithubOrgClient("google")
            repos = google.public_repos(license='MIT')
            expected_repos = ["repo1"]

            self.assertEqual(repos, expected_repos)
            self.assertTrue(google._public_repos_url)
            get_mock.assert_called_once_with(google._public_repos_url)

