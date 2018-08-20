"""
================================================
Collocation Toolkit (:mod:`typhon.collocations`)
================================================

This module contains classes to find collocations between datasets.
They are inspired by the implemented ``CollocatedDataset`` classes
in ``atmlab`` written by Gerrit Holl.

.. module:: typhon.collocations

.. automodule:: typhon.collocations.common

.. codeauthor:: John Mrziglod, June 2017
"""

from .collocator import *  # noqa
from .common import *  # noqa

__all__ = [s for s in dir() if not s.startswith('_')]
