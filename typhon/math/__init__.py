"""
=========================
Math (:mod:`typhon.math`)
=========================

Mathematical functions and modules.

.. module:: typhon.math

.. automodule:: typhon.math.common

.. automodule:: typhon.math.array

.. automodule:: typhon.math.stats

"""

from typhon.math.array import *  # noqa
from typhon.math.common import *  # noqa
from typhon.math.stats import *  # noqa

__all__ = [s for s in dir() if not s.startswith('_')]
