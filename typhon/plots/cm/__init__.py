"""
=========
Colormaps
=========

This module provides colormaps to use for the visualisation of meteorological
data.

This module heavily bases on the cmocean_ package developed by Kristen Thyng.
Most colormaps are directly inherited and renamed for meteorological
applications.

.. _cmocean: http://matplotlib.org/cmocean/

Example gallery
------------------

Typhon Colormaps
^^^^^^^^^^^^^^^^
.. plot:: pyplots/cm_gallery.py

Density
^^^^^^^
.. plot:: pyplots/plot_density.py
    :include-source:

Difference
^^^^^^^^^^
.. plot:: pyplots/plot_difference.py
    :include-source:

Max-Planck
^^^^^^^^^^
.. plot:: pyplots/plot_max-planck.py
    :include-source:

Phase
^^^^^
.. plot:: pyplots/plot_phase.py
    :include-source:

Qualitative 1
^^^^^^^^^^^^^
.. plot:: pyplots/plot_qualitative1.py
    :include-source:

Qualitative 2
^^^^^^^^^^^^^
.. plot:: pyplots/plot_qualitative2.py
    :include-source:

Speed
^^^^^
.. plot:: pyplots/plot_speed.py
    :include-source:

Temperature
^^^^^^^^^^^
.. plot:: pyplots/plot_temperature.py
    :include-source:

Velocity
^^^^^^^^
.. plot:: pyplots/plot_velocity.py
    :include-source:

Vorticity
^^^^^^^^^
.. plot:: pyplots/plot_vorticity.py
    :include-source:

"""
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.cm import register_cmap

from ._cmocean import datad as _cmocean_datad
from ._cm import datad as _cm_datad


datad = _cmocean_datad
datad.update(_cm_datad)


def _rev_cdict(cdict):
    """Revert a dictionary containing specs for a LinearSegmentedColormap."""
    rev_cdict = {}
    for k, v in cdict.items():
        rev_cdict[k] = [(1.0 - x, y1, y0) for x, y0, y1 in reversed(v)]
    return rev_cdict

cmaps = {}
for (name, data) in datad.items():
    if 'red' in data:
        cmaps[name] = LinearSegmentedColormap(name, data)
        cmaps[name + '_r'] = LinearSegmentedColormap(
            name + '_r', _rev_cdict(data))
    else:
        cmaps[name] = LinearSegmentedColormap.from_list(
            name, data, N=len(data))
        cmaps[name + '_r'] = LinearSegmentedColormap.from_list(
            name + '_r', data[::-1], N=len(data))

locals().update(cmaps)

for name, cm in cmaps.items():
    register_cmap(name, cm)

__all__ = list(cmaps.keys())
