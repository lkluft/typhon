"""
.. _typhon-handlers:

Handlers
========

This package provides file handler classes. The file handler classes provide
specialized reading (sometimes as well writing) methods for several data
formats.

.. currentmodule:: typhon.files

.. automodule:: typhon.files.handlers.common

File handlers for satellite products
++++++++++++++++++++++++++++++++++++

.. currentmodule:: typhon.files

.. autosummary::
   :toctree: generated

   CloudSat
   HOAPS
   AAPP_HDF
   AVHRR_GAC_HDF
   MHS_HDF
   SEVIRI

File handlers for other products
++++++++++++++++++++++++++++++++

.. automodule:: typhon.files.handlers.ocean_rain

"""

from .common import *  # noqa
from .cloudsat import *  # noqa
from .hoaps import *  # noqa
from .meteosat import *
from .ocean_rain import *  # noqa
from .tovs import *  # noqa