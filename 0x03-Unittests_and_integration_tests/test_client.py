#!/usr/bin/env python3
"""Parameterize and patch as decorators"""

import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test class for GithubOrgClient"""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch("client.get_json", return_value={"login": "mocked_org"})
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value"""
        client = GithubOrgClient(org_name)

        result = client.org

        url_format = f"https://api.github.com/orgs/{org_name}"

        mock_get_json.assert_called_once_with(url_format)

        self.assertEqual(result, {"login": "mocked_org"})

        def test_public_repos_url(self):
        """Test that GithubOrgClient._public_repos_url returns the expected result"""
        mock_payload = {
            "repos_url": "https://api.github.com/orgs/test_org/repos"
        }

        with patch.object(GithubOrgClient, 'org', return_value=mock_payload):
            client = GithubOrgClient("test_org")
            result = client._public_repos_url

            self.assertEqual(result, "https://api.github.com/orgs/test_org/repos")


if __name__ == "__main__":
    unittest.main()
