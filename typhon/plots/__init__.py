"""
==============================
Plotting (:mod:`typhon.plots`)
==============================

This module provides functions related to plot or to plot data.

.. module:: typhon.plots

.. automodule:: typhon.plots.common

.. automodule:: typhon.plots.colors

.. automodule:: typhon.plots.formatter

.. automodule:: typhon.plots.maps

.. automodule:: typhon.plots.plots

.. automodule:: typhon.plots.arts_lookup

Typhon style sheet
==================

.. plot:: pyplots/stylesheet_gallery.py
    :include-source:

"""

from typhon.plots import cm  # noqa
from typhon.plots.colors import *  # noqa
from typhon.plots.common import *  # noqa
from typhon.plots.formatter import *  # noqa
from typhon.plots.plots import *  # noqa
from typhon.plots.arts_lookup import *  # noqa
try:
    from typhon.plots.maps import *  # noqa
except ImportError:
    pass

__all__ = [s for s in dir() if not s.startswith('_')]
