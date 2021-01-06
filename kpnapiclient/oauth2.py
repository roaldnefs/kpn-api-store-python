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

import requests


class OAuth2Token(dict):
    """Represents an OAuth2 client token."""

    @classmethod
    def from_dict(klass, data):
        return klass(data)


class OAuth2Client:
    """Represents an OAuth2 client."""

    def __init__(self, client_id: str, client_secret: str) -> None:
        self._client_id: str = client_id
        self._client_secret: str = client_secret

    def fetch_token(self, url: str, grant_type: str):
        """Fetch an access token from the token endpoint."""
        params = dict(grant_type=grant_type)
        data = dict(
            client_id=self._client_id, client_secret=self._client_secret
        )

        session: requests.Session = requests.Session()
        req: requests.Request = requests.Request(
            "POST", url, data=data, params=params
        )
        prepped: requests.PreparedRequest = req.prepare()
        resp: requests.Response = session.send(prepped)

        return OAuth2Token.from_dict(resp.json())
