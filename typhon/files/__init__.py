"""
===================================
File handling (:mod:`typhon.files`)
===================================

This module contains convenience functions for general file handling.

.. module:: typhon.files

.. automodule:: typhon.files.utils

.. automodule:: typhon.files.fileset

.. automodule:: typhon.files.handlers

"""

from .fileset import *
from .handlers import *
from .utils import *

__all__ = [s for s in dir() if not s.startswith('_')]