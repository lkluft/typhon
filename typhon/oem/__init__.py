"""
=======================
OEM (:mod:`typhon.oem`)
=======================

Functions related to the Optimal Estimation Method (OEM).

.. module:: typhon.oem

.. automodule:: typhon.oem.common

.. automodule:: typhon.oem.error

"""

from typhon.oem.common import *  # noqa
from typhon.oem.error import *  # noqa


__all__ = [s for s in dir() if not s.startswith('_')]
