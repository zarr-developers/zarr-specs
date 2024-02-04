======================
Xarray Zarr Convention
======================

+---------------------+----------------------+
| Convention Type     | Legacy               |
+---------------------+----------------------+
| Zarr Spec Versions  | V2                   |
+---------------------+----------------------+
| Status              | Active               |
+---------------------+----------------------+
| Active Dates        | 2018 - present       |
+---------------------+----------------------+
| Version             | 1                    |
+---------------------+----------------------+

See also `Zarr Encoding Specification <https://docs.xarray.dev/en/latest/internals/zarr-encoding-spec.html>`_
in the Xarray docs.


Description
-----------

`Xarray`_ is a Python library for working with labeled multi-dimensional arrays.
Xarray was originally designed to read only `NetCDF`_ files, but has since added support for
other formats.
In implementing support for the `Zarr <https://zarr.dev>`_ storage format, Xarray developers
made some *ad hoc* choices about how to store NetCDF-style data in Zarr.
These choices have become a de facto convention for mapping the Zarr data model to the
`NetCDF data model <https://docs.unidata.ucar.edu/netcdf-c/current/netcdf_data_model.html>`_

First, Xarray can only read and write Zarr groups. There is currently no support
for reading / writing individual Zarr arrays. Zarr groups are mapped to
Xarray ``Dataset`` objects, which correspond to NetCDF-4 / HDF5 groups.

Second, from Xarray's point of view, the key difference between
NetCDF and Zarr is that all NetCDF arrays have *dimension names* while Zarr
arrays do not. Therefore, in order to store NetCDF data in Zarr, Xarray must
somehow encode and decode the name of each array's dimensions.

To accomplish this, Xarray developers decided to define a special Zarr array
attribute: ``_ARRAY_DIMENSIONS``. The value of this attribute is a list of
dimension names (strings), for example ``["time", "lon", "lat"]``. When writing
data to Zarr, Xarray sets this attribute on all variables based on the variable
dimensions. When reading a Zarr group, Xarray looks for this attribute on all
arrays, raising an error if it can't be found. The attribute is used to define
the variable dimension names and then removed from the attributes dictionary
returned to the user.

Because of these choices, Xarray cannot read arbitrary array data, but only
Zarr data with valid ``_ARRAY_DIMENSIONS`` attributes on each array.

After decoding the ``_ARRAY_DIMENSIONS`` attribute and assigning the variable
dimensions, Xarray proceeds to [optionally] decode each variable using its
standard `CF Conventions`_ decoding machinery used for NetCDF data.

Finally, it's worth noting that Xarray writes (and attempts to read)
"consolidated metadata" by default (the ``.zmetadata`` file), which is another
non-standard Zarr extension, albeit one implemented upstream in Zarr-Python.

.. _Xarray: http://xarray.dev
.. _NetCDF: https://www.unidata.ucar.edu/software/netcdf
.. _CF Conventions: http://cfconventions.org


Identifying the Presence of this Convention
-------------------------------------------

In implementing this convention, Xarray developers made the unfortunate choice of not
including any explicit identifier in the Zarr metadata. Therefore, the only way to
determine whether the convention is being used is to attempt to examine contents of the
Zarr dataset and look for the following properties:

* A single flat group containing one or more arrays
* The presence of the ``_ARRAY_DIMENSIONS`` attribute on each array, whose contents are
  a list of dimension names (strings)
* If the dimension name corresponds to another array name within the group, that array is
  assumed to be a dimension coordinate. Dimension coordinates arrays must be 1D
  and have the same length as the corresponding dimension.


CF Conventions
--------------

It is common for data stored in Zarr using the Xarray convention to also follow
the `Climate and Forecast (CF) Metadata Conventions <CF Conventions>`_.

A high-level description of these conventions, quoted from the CF Documentation is as follows:

    The NetCDF library [NetCDF] is designed to read and write data that has been structured
    according to well-defined rules and is easily ported across various computer platforms.
    The netCDF interface enables but does not require the creation of self-describing datasets.
    The purpose of the CF conventions is to require conforming datasets to contain sufficient
    metadata that they are self-describing in the sense that each variable in the file has an
    associated description of what it represents, including physical units if appropriate,
    and that each value can be located in space (relative to earth-based coordinates) and time.

The CF Conventions are massive and cover a wide range of topics. Readers should consult the
`CF Conventions`_ documentation for more information.