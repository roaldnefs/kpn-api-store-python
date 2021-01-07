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

from typing import Optional


class KpnError(Exception):

    def __init__(self, message: str = "") -> None:
        super().__init__(message)
        self.message = message

    def __str__(self) -> str:
        return self.message


class KpnHTTPError(KpnError):

    def __init__(
        self,
        message: str = "",
        response_code: Optional[int] = None
    ) -> None:
        super().__init__(message)
        self.response_code = response_code

    def __str__(self) -> str:
        if self.response_code:
            return f"{self.response_code}: {self.message}"
        else:
            return self.message


class KpnParsingError(KpnError):
    pass
