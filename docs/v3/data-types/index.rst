.. _data-types-list:

==========
Data Types
==========

The following section specifies data types which SHOULD
be implemented by all implementations.

Core data types
---------------

.. list-table:: Data types
   :header-rows: 1

   * - Identifier
     - Numerical Type
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

.. _fill-value-list:

Permitted fill values
^^^^^^^^^^^^^^^^^^^^^

The permitted values depend on the data type:

    ``bool``
      The value must be a JSON boolean (``false`` or ``true``).

    Integers (``{uint,int}{8,16,32,64}``)
      The value must be a JSON number with no fraction or exponent part that is
      within the representable range of the data type.

    IEEE 754 floating point numbers (``float{16,32,64}``)
      The value may be either:

      - A JSON number, that will be rounded to the nearest representable value.

      - A JSON string of the form:

        - ``"Infinity"``, denoting positive infinity;
        - ``"-Infinity"``, denoting negative infinity;
        - ``"NaN"``, denoting thenot-a-number (NaN) value where the sign bit is
          0 (positive), the most significant bit (MSB) of the mantissa is 1, and
          all other bits of the mantissa are zero;
        - ``"0xYYYYYYYY"``, specifying the byte representation of the floating
          point number as an unsigned integer.  For example, for ``float32``,
          ``"NaN"`` is equivalent to ``"0x7fc00000"``.  This representation is
          the only way to specify a NaN value other than the specific NaN value
          denoted by ``"NaN"``.

        .. warning::

           While this NaN syntax is consistent with the syntax accepted by the
           C99 ``strtod`` function, C99 leaves the meaning of the NaN payload
           string implementation defined, which may not match the Zarr
           definition.

    Complex numbers (``complex{64,128}``)
      The value must be a two-element array, specifying the real and imaginary
      components respectively, where each component is specified as defined
      above for floating point number.

      For example, ``[1, 2]`` indicates ``1 + 2i`` and ``["-Infinity", "NaN"]``
      indicates a complex number with real component of -inf and imaginary
      component of NaN.

    Raw data types (``r<N>``)
      An array of integers, with length equal to ``<N>``, where each integer is
      in the range ``[0, 255]``.

Extensions
----------

Registered data type extensions can be found under
`zarr-extensions::data-types <https://github.com/zarr-developers/zarr-extensions/tree/main/data-types>`_.
