.. _bytes-codec-v1:

============================
 Bytes codec (version 1.0)
============================

  **Editor's draft 26 July 2019**

Specification URI:
    https://zarr-specs.readthedocs.io/en/latest/v3/codecs/bytes/
Corresponding ZEP:
    `ZEP0001 — Zarr specification version 3 <https://zarr.dev/zeps/accepted/ZEP0001.html>`_
Issue tracking:
    `GitHub issues <https://github.com/zarr-developers/zarr-specs/labels/codec>`_
Suggest an edit for this spec:
    `GitHub editor <https://github.com/zarr-developers/zarr-specs/blob/main/docs/v3/codecs/bytes/index.rst>`_

Copyright 2020-Present Zarr core development team. This work
is licensed under a `Creative Commons Attribution 3.0 Unported License
<https://creativecommons.org/licenses/by/3.0/>`_.

----


Abstract
========

Defines an ``array -> bytes`` codec that encodes arrays of fixed-size numeric
data types as a sequence of bytes in lexicographical order. For multi-byte data
types, it encodes the array either in little endian or big endian.


Status of this document
=======================

ZEP0001 was accepted on May 15th, 2023 via https://github.com/zarr-developers/zarr-specs/issues/227.


Document conventions
====================

Conformance requirements are expressed with a combination of
descriptive assertions and [RFC2119]_ terminology. The key words
"MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD",
"SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in the normative
parts of this document are to be interpreted as described in
[RFC2119]_. However, for readability, these words do not appear in all
uppercase letters in this specification.

All of the text of this specification is normative except sections
explicitly marked as non-normative, examples, and notes. Examples in
this specification are introduced with the words "for example".


Codec name
==========

The value of the ``name`` member in the codec object MUST be ``bytes``.


Configuration parameters
========================

endian:
    Required for data types for which endianness is applicable. For example, 
    this includes multi-byte data types, such as ``uint16`` and ``int32``, 
    but not single-byte data types, such as ``uint8`` or ``bool``. 
    If present, the value MUST be a string equal to either ``"big"`` or 
    ``"little"``.


Format and algorithm
====================

This is an ``array -> bytes`` codec.

Each element of the array is encoded using the specified endian variant of its
binary representation listed below.  Array elements are encoded in
lexicographical order.  For example, with ``endian`` specified as ``big``, the
``int32`` data type is encoded as a 4-byte big endian two's complement integer,
and the ``complex128`` data type is encoded as two consecutive 8-byte big endian
IEEE 754 binary64 values.

.. list-table:: Supported data types
   :header-rows: 1

   * - Identifier
     - Binary representation
   * - ``bool``
     - Single byte, with false encoded as ``\\x00`` and true encoded as
       ``\\x01``.  Does not depend on ``endian`` parameter.
   * - ``int8``
     - 1 byte two's complement.  Does not depend on ``endian`` parameter.
   * - ``int16``
     - 2-byte two's complement
   * - ``int32``
     - 4-byte two's complement
   * - ``int64``
     - 8-byte two's complement
   * - ``uint8``
     - 1 byte.  Does not depend on ``endian`` parameter.
   * - ``uint16``
     - 2-byte
   * - ``uint32``
     - 4-byte
   * - ``uint64``
     - 8-byte
   * - ``float16`` (optionally supported)
     - 2-byte IEEE 754 binary16
   * - ``float32``
     - 4-byte IEEE 754 binary32
   * - ``float64``
     - 8-byte IEEE 754 binary64
   * - ``complex64``
     - 2 consecutive 4-byte IEEE 754 binary32 values (real component followed by imaginary component)
   * - ``complex128``
     - 2 consecutive 8-byte IEEE 754 binary64 values (real component followed by imaginary component)
   * - ``r*``
     - number of bits, which must be a multiple of 8, given by ``*``.

.. note::

   To encode elements in a different order than lexicographical order (C
   order/row major), the :ref:`transpose codec<transpose-codec-v1>` may be
   specified.

References
==========

.. [RFC2119] S. Bradner. Key words for use in RFCs to Indicate
   Requirement Levels. March 1997. Best Current Practice. URL:
   https://tools.ietf.org/html/rfc2119


Change log
==========

- ``endian`` codec was renamed to ``bytes`` codec.  `PR #263
  <https://github.com/zarr-developers/zarr-specs/pull/263/>`_
