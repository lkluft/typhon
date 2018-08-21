"""
Marcov Chain Monte Carlo (:mod:`typhon.retrieval.mcmc`)
=======================================================

This subpackage provides functionality to sample posterior distributions of
inverse problems in atmospheric soundings using ARTS as forward model.

.. currentmodule:: typhon.retrieval.mcmc

The main functionality is implemented by the :class:`MCMC` class which
implements the Metropolis algorithm to sample from the posterior distribution.

In addition to that this subpackage provides a `RandomWalk` class that
simplifies the setup of random walk jump functions as well as diagnostic
function to assess mixing and convergence of the simulations.

.. automodule:: typhon.retrieval.mcmc.mcmc

.. automodule:: typhon.retrieval.mcmc.jumping_rules

"""
from typhon.retrieval.mcmc.mcmc import *  # noqa
from typhon.retrieval.mcmc.jumping_rules import RandomWalk
