.. _data-types-list:

==========
Data Types
==========

The following data types are defined by the maintainers of
the Zarr specification. Being listed below does not imply that a data type is
required to be implemented by implementations.

Core data types
---------------

.. list-table:: Data types
   :header-rows: 1

   * - Identifier
     - Numerical type
   * - ``bool``
     - Boolean
   * - ``int8``
     - Integer in ``[-2^7, 2^7-1]``
   * - ``int16``
     - Integer in ``[-2^15, 2^15-1]``
   * - ``int32``
     - Integer in ``[-2^31, 2^31-1]``
   * - ``int64``
     - Integer in ``[-2^63, 2^63-1]``
   * - ``uint8``
     - Integer in ``[0, 2^8-1]``
   * - ``uint16``
     - Integer in ``[0, 2^16-1]``
   * - ``uint32``
     - Integer in ``[0, 2^32-1]``
   * - ``uint64``
     - Integer in ``[0, 2^64-1]``
   * - ``float16`` (optionally supported)
     - IEEE 754 half-precision floating point: sign bit, 5 bits exponent, 10 bits mantissa
   * - ``float32``
     - IEEE 754 single-precision floating point: sign bit, 8 bits exponent, 23 bits mantissa
   * - ``float64``
     - IEEE 754 double-precision floating point: sign bit, 11 bits exponent, 52 bits mantissa
   * - ``complex64``
     - real and complex components are each IEEE 754 single-precision floating point
   * - ``complex128``
     - real and complex components are each IEEE 754 double-precision floating point
   * - ``r*`` (Optional)
     - raw bits, variable size given by ``*``, limited to be a multiple of 8

Extensions
----------

Registered data type extensions can be found under
`zarr-extensions::data-types <https://github.com/zarr-developers/zarr-extensions/tree/main/data-types>`_.
