# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Roald Nefs <info@roaldnefs.com>
#
# This file is part of kpn-api-store-python.
#
# kpn-api-store-python is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# kpn-api-store-python is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with kpn-api-store-python. If not, see
# <https://www.gnu.org/licenses/>.

import responses  # type: ignore
import unittest

from kpnapistore.base import Client as BaseClient
from tests.utils import register_responses_fixtures


class BaseClientTest(unittest.TestCase):
    """Test the base KPN API Store Client class."""

    client: BaseClient

    @classmethod
    @responses.activate
    def setUpClass(self) -> None:
        """Set up a base KPN API Store client."""
        register_responses_fixtures('auth.json')

        # Initialize a base KPN API Store client
        self.client = BaseClient('APP_CLIENT_ID', 'APP_CLIENT_SECRET')

    def test_base_url(self) -> None:
        """Test the base URL of the API."""
        url: str = self.client.url

        self.assertEqual(url, "https://api-prd.kpn.com")

    def test_access_token(self) -> None:
        """Test if the OAuth2 token has been set correctly."""
        # TODO(roaldnefs): Test is token is set, because is can be empty.
        access_token: str = self.client._token["access_token"]  # type: ignore
        token_type: str = self.client._token["token_type"]  # type: ignore

        self.assertEqual(access_token, "staG765sBUuai4OMeZiTful6PTRt")
        self.assertEqual(token_type, "Bearer")

    def test_authorization_header(self) -> None:
        """Test if the Authorization header is set correctly."""
        auth_header: str = self.client._headers["Authorization"]

        self.assertEqual(auth_header, "Bearer staG765sBUuai4OMeZiTful6PTRt")
