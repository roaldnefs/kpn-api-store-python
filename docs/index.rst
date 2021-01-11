.. kpn-api-store-python documentation master file, created by
   sphinx-quickstart on Mon Jan 11 20:21:32 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. image:: https://github.com/roaldnefs/kpn-api-store-python/blob/main/cover.png?raw=true
   :target: https://github.com/roaldnefs/kpn-api-store-python

Release v\ |version|. (:ref:`Installation <install>`)

.. image:: https://img.shields.io/pypi/pyversions/kpn-api-store?color=090&logo=python&logoColor=white&style=for-the-badge
   :target: https://pypi.org/project/kpn-api-store/
.. image:: https://img.shields.io/pypi/dm/kpn-api-store?color=090&logo=python&logoColor=white&style=for-the-badge
   :target: https://pypi.org/project/kpn-api-store/
.. image:: https://img.shields.io/pypi/format/kpn-api-store?color=090&logo=python&logoColor=white&style=for-the-badge
   :target: https://pypi.org/project/kpn-api-store/
.. image:: https://img.shields.io/github/license/roaldnefs/kpn-api-store-python?color=090&style=for-the-badge
   :target: https://raw.githubusercontent.com/roaldnefs/kpn-api-store-python/main/COPYING.LESSER
.. image:: https://img.shields.io/github/workflow/status/roaldnefs/kpn-api-store-python/tests?color=090&label=CI&logo=github&style=for-the-badge
   :target: https://github.com/roaldnefs/kpn-api-store-python/actions
.. image:: https://img.shields.io/github/contributors/roaldnefs/kpn-api-store-python?color=090&logo=github&style=for-the-badge
   :target: https://github.com/roaldnefs/kpn-api-store-python/graphs/contributors

**kpn-api-store-python** is the Python client library for APIs provided by the `KPN API Store <https://developer.kpn.com/>`_.

-------------------

**Example usage**::

    # Import the KPN-SMS API client
    from kpnapistore.messaging.sms_kpn.v1 import Client

    # Initialize a new KPN-SMS API client using the OAuth 2.0 Client Credentials
    # Grant type `Client ID` and `Client secret`
    client = Client("APP_CLIENT_ID", "APP_CLIENT_SECRET")

    # Send a SMS
    client.send("KPN API", "316xxxxxxxx", "Hello from kpn-api-store-python!")

The User Guide
--------------

.. toctree::
   :maxdepth: 2

   user/install
