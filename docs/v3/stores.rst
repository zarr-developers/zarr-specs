.. _stores-list:

======
Stores
======

The following documents specify core stores which are defined by the maintainers of the Zarr specification.
Being listed below does not imply that a store is required to be implemented by all implementations.

.. toctree::
   :glob:
   :maxdepth: 1
   :titlesonly:
   :caption: Contents:

   stores/*/*

.. note::
   Stores are *not* extension points since they define the mechanism
   for loading metadata documents such that extensions can be loaded.
