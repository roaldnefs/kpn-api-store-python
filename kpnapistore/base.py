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
"""Wrapper for APIs provided by the KPN API Store."""

import requests

from typing import Optional, Any, Dict, Union

from kpnapistore import __title__, __version__
from kpnapistore.exceptions import KpnHTTPError, KpnParsingError


class OAuth2Token(dict):
    """Represents an OAuth2 client token."""

    @classmethod
    def from_dict(klass, data):
        return klass(data)


class Client:
    """Represents a KPN API Store client.

    Args:
        client_id (str): The OAuth2 client ID.
        client_secret (str): The OAuth2 client secret.
    """

    _base_api_path: Optional[str] = None

    def __init__(self, client_id, client_secret):
        self._base_url = "https://api-prd.kpn.com"
        self._token: Optional[OAuth2Token] = None

        # Headers to use when making a request to the KPN APIs
        self._headers: Dict[str, str] = {
            "User-Agent": f"{__title__}/{__version__}",
        }

        # Initialize a session object for making requests
        self._session: requests.Session = requests.Session()

        self._client_id: str = client_id
        self._client_secret: str = client_secret
        self._grant_type: str = "client_credentials"
        self._set_auth_info()

    @property
    def url(self) -> str:
        """Return the API URL."""
        return self._base_url

    def _set_auth_info(self) -> None:
        """Authenticate and set the authorization header."""

        self._token = self._fetch_oauth2_token()

        # Set the authorization header
        token_type: str = self._token["token_type"]
        access_token: str = self._token["access_token"]
        self._headers["Authorization"] = f"{token_type} {access_token}"

    def _build_url(self, path: str) -> str:
        """Return the full URL."""
        if path.startswith("http://") or path.startswith("https://"):
            return path
        return f"{self._base_url}{self._base_api_path or ''}{path}"

    def _fetch_oauth2_token(self) -> OAuth2Token:
        """Fetch an OAuth2 token from the KPN API Store."""
        path: str = f"{self._base_url}/oauth/client_credential/accesstoken"
        params: Dict[str, str] = dict(grant_type=self._grant_type)
        payload: Dict[str, str] = dict(
            client_id=self._client_id, client_secret=self._client_secret
        )

        result = self.post(path, data=payload, params=params)

        if isinstance(result, dict):
            return OAuth2Token.from_dict(result)
        else:
            raise KpnParsingError(
                "Failed to parse the API response as OAuth2 token"
            )

    def _get_headers(self, content_type: Optional[str] = None):
        headers = self._headers.copy()
        if content_type:
            headers["Content-Type"] = content_type
        return headers

    def request(
        self,
        method: str,
        path: str,
        data: Optional[Any] = None,
        json: Optional[Any] = None,
        params: Optional[Dict[str, Any]] = None
    ) -> Union[requests.Response, Dict[str, Any]]:
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
            KpnParsingError: When the content can not be parsed as json
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

        prepped: requests.PreparedRequest = self._session.prepare_request(
            request
        )
        response: requests.Response = self._session.send(prepped)

        if 200 <= response.status_code < 300:
            if response.headers.get("Content-Type") == "application/json":
                try:
                    return response.json()
                except Exception:
                    raise KpnParsingError(
                        message="Failed to parse the API response as JSON"
                    )
            return response

        # TODO(roaldnefs): Extract error message from the API response.
        raise KpnHTTPError(
            message=str(response.content),
            response_code=response.status_code
        )

    def post(
        self,
        path: str,
        data: Optional[Any] = None,
        json: Optional[Any] = None,
        params: Optional[Dict[str, Any]] = None
    ) -> Any:
        """Make a POST request to the KPN API Store.

        Args:
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
        return self.request(
            "POST", path, data=data, json=json, params=params
        )
