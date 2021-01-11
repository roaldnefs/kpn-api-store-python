.. _install:

Installation of kpn-api-store-python
====================================

This part of the documentation covers the installation of `kpn-api-store-python`.
The first step to using any software package is getting it properly installed.

Using pip
---------

To install kpn-api-store-python, simply run this simple command in your terminal of
choice::

    $ python -m pip install kpn-api-store

Get the Source Code
-------------------

kpn-api-store-python is actively developed on GitHub, where the code is
`available <https://github.com/roaldnefs/kpn-api-store-python>`_.

You can either clone the public repository::

    $ git clone git://github.com/roaldnefs/kpn-api-store-python.git

Or, download the `tarball <https://github.com/roaldnefs/kpn-api-store-python/tarball/master>`_::

    $ curl -OL https://github.com/roaldnefs/kpn-api-store-python/tarball/master
    # optionally, zipball is also available (for Windows users).

Once you have a copy of the source, you can embed it in your own Python
package, or install it into your site-packages easily::

    $ cd kpn-api-store-python
    $ python -m pip install .
