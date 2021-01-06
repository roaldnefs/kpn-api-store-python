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
"""Wrapper for APIs provided by the KPN API Store."""

import requests

from typing import Optional, Any, Dict

from kpnapiclient.oauth2 import OAuth2Client, OAuth2Token
from kpnapiclient.exceptions import KpnHTTPError, KpnParsingError


__title__ = "kpn-api-python-client"
__version__ = "0.1.0"
__author__ = "Roald Nefs"
__email__ = "info@roaldnefs.com"
__copyright__ = "Copyright 2021, Roald Nefs"
__license__ = "LGPL3"


class Kpn(OAuth2Client):
    """Represents a KPN API Store connection.

    Args:
        client_id (str): The OAuth2 client ID.
        client_secret (str): The OAuth2 client secret.
    """

    def __init__(self, client_id, client_secret):
        super().__init__(client_id, client_secret)

        self._base_url = "https://api-prd.kpn.com"
        self._token: Optional[OAuth2Token] = None

        # Headers to use when making a request to the KPN APIs
        self.headers: Dict[str, str] = {
            "User-Agent": f"{__title__}/{__version__}",
        }

        # Initialize a session object for making requests
        self.session: requests.Session = requests.Session()

    @property
    def url(self) -> str:
        """Return the API URL."""
        return self._base_url

    @property
    def token(self) -> OAuth2Token:
        """Return the OAuth2Token."""
        if not self._token:
            self._token = self._fetch_token()
        return self._token

    def _build_url(self, path: str) -> str:
        return f"{self._base_url}{path}"

    def _fetch_token(self) -> OAuth2Token:
        """Fetch an access token from the KPN API Store."""
        url: str = self._build_url("/oauth/client_credential/accesstoken")
        grant_type: str = "client_credentials"
        return self.fetch_token(url, grant_type=grant_type)

    def _get_headers(self, content_type: Optional[str] = None):
        headers = self.headers.copy()
        if content_type:
            headers["Content-Type"] = content_type

        # Set authorization header
        token_type: str = self.token["token_type"]
        access_token: str = self.token["access_token"]
        headers["Authorization"] = f"{token_type} {access_token}"

        return headers

    def _request(
        self,
        method: str,
        path: str,
        data: Optional[Any] = None,
        json: Optional[Any] = None,
        params: Optional[Dict[str, Any]] = None
    ) -> requests.Response:
        """Make an HTTP request to the KPN API Store.

        Args:
            method (str): HTTP method to use
            path (str): The path to append to the API URL
            data (dict): The body to attach to the request
            json (dict): The json body to attach to the request
            params (dict): URL parameters to append to the URL

        Returns:
            A requests response object.

        Raises:
            KpnHTTPError: When the return code of the request is not 2xx
        """
        url: str = self._build_url(path)

        # Set the content type for the request if json is provided and data is
        # not specified
        content_type: Optional[str] = None
        if not data and json:
            content_type = "application/json"

        headers: Dict[str, str] = self._get_headers(content_type)
        request: requests.Request = requests.Request(
            method, url, headers=headers, data=data, json=json, params=params,
        )

        prepped: requests.PreparedRequest = self.session.prepare_request(
            request
        )
        response: requests.Response = self.session.send(prepped)

        if 200 <= response.status_code < 300:
            return response

        # TODO(roaldnefs): Extract error message from the API response.
        raise KpnHTTPError(
            message=str(response.content),
            response_code=response.status_code
        )

    def request(
        self,
        method: str,
        path: str,
        data: Optional[Any] = None,
        json: Optional[Any] = None,
        params: Optional[Dict[str, Any]] = None
    ) -> Any:
        """Make an HTTP request to the KPN API Store.

        Args:
            method (str): HTTP method to use
            path (str): The path to append to the API URL
            data (dict): The body to attach to the request
            json (dict): The json body to attach to the request
            params (dict): URL parameters to append to the URL

        Returns:
            Returns the json-encoded content of a response, if any.

        Raises:
            KpnHTTPError: When the return code of the request is not 2xx
            KpnParsingError: When the response content can not be parsed as
                JSON
        """
        response: requests.Response = self._request(
            method, path, data=data, json=json, params=params
        )

        if response.text:
            try:
                return response.json()
            except Exception:
                raise KpnParsingError(
                    message="Failed to parse the API response as JSON"
                )
        return None
