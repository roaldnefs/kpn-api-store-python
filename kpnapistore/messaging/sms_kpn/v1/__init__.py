# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Roald Nefs <info@roaldnefs.com>
#
# This file is part of kpn-api-python-client.
#
# kpn-api-python-client is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# kpn-api-python-client is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with kpn-api-python-client. If not, see
# <https://www.gnu.org/licenses/>.
"""Wrapper for the KPN SMS API."""

from typing import Dict, Any

from kpnapistore.base import Client as BaseClient


class Client(BaseClient):

    _base_api_path: str = "/messaging/sms-kpn/v1"

    def send(
        self,
        sender: str,
        mobile_number: str,
        content: str
    ) -> Dict[str, Any]:
        """Send an SMS.

        Args:
            sender (str):
            mobile_number (str):
            content: (str):

        Returns:
            dict:

        Raises:
            KpnHTTPError: When the return code of the request is not 2xx
            KpnParsingError: When the content can not be parsed as json
        """
        path: str = "/send"
        payload: Dict[str, Any] = {
            "sender": sender,
            "messages": [{
                "mobile_number": mobile_number,
                "content": content
            }]
        }

        return self.post(path, json=payload)
