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

from typing import Dict

import responses  # type: ignore
import unittest

from kpnapistore.messaging.sms_kpn.v1 import Client
from tests.utils import register_responses_fixtures


class BaseClientTest(unittest.TestCase):
    """Test SMS-KPN APi."""

    client: Client

    @classmethod
    @responses.activate
    def setUpClass(cls) -> None:
        """Set up SMS-KPN API client."""
        register_responses_fixtures('auth.json')

        # Initialize a base KPN API Store client
        cls.client = Client('APP_CLIENT_ID', 'APP_CLIENT_SECRET')

    def setUp(self) -> None:
        """Register mocked responses."""
        register_responses_fixtures('sms-kpn.json')

    @responses.activate
    def test_send(self) -> None:
        """Test sending a text message."""
        data: Dict[str, str] = self.client.send(
            "KPN API", "0600000000", "Hi from KPN!"
        )

        self.assertEqual(
            data["document_id"],
            "b4e905d4-774c-4c83-8360-01427e17a33a"
        )
