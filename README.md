# kpn-api-store-python

[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/kpn-api-store?color=090&logo=python&logoColor=white&style=for-the-badge)](https://pypi.org/project/kpn-api-store/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/kpn-api-store?color=090&logo=python&logoColor=white&style=for-the-badge)](https://pypi.org/project/kpn-api-store/)
[![PyPI - Format](https://img.shields.io/pypi/format/kpn-api-store?color=090&logo=python&logoColor=white&style=for-the-badge)](https://pypi.org/project/kpn-api-store/)
[![License](https://img.shields.io/github/license/roaldnefs/kpn-api-store-python?color=090&style=for-the-badge)](https://raw.githubusercontent.com/roaldnefs/kpn-api-store-python/main/COPYING)
[![GitHub Workflow Status](https://img.shields.io/github/workflow/status/roaldnefs/kpn-api-store-python/tests?color=090&label=CI&logo=github&style=for-the-badge)](https://github.com/roaldnefs/kpn-api-store-python/actions)
[![GitHub contributors](https://img.shields.io/github/contributors/roaldnefs/kpn-api-store-python?color=090&logo=github&style=for-the-badge)](https://github.com/roaldnefs/kpn-api-store-python/graphs/contributors)

**kpn-api-store-python** is the Python client library for APIs provided by the [KPN API Store](https://developer.kpn.com/).

```python
from kpnapistore.messaging.sms_kpn.v1 import Client


client_id = "APP_CLIENT_ID"
client_secret = "APP_CLIENT_SECRET"

client = Client(client_id, client_secret)
client.send("KPN API", "316xxxxxxxx", "Hello from kpn-api-store-python!")
```
