==========
Gzip codec
==========

Version:
    1.0
Specification URI:
    https://zarr-specs.readthedocs.io/en/latest/v3/codecs/gzip/
Corresponding ZEP:
    `ZEP0001 — Zarr specification version 3 <https://zarr.dev/zeps/accepted/ZEP0001.html>`_
Issue tracking:
    `GitHub issues <https://github.com/zarr-developers/zarr-specs/labels/codec>`_
Suggest an edit for this spec:
    `GitHub editor <https://github.com/zarr-developers/zarr-specs/blob/main/docs/v3/codecs/gzip/index.rst>`_

Copyright 2020-Present Zarr core development team. This work
is licensed under a `Creative Commons Attribution 3.0 Unported License
<https://creativecommons.org/licenses/by/3.0/>`_.

----


Abstract
========

Defines a ``bytes -> bytes`` codec that applies gzip compression.


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

The value of the ``name`` member in the codec object MUST be ``gzip``.


Configuration parameters
========================

level:
    An integer from 0 to 9 which controls the speed and level of
    compression. A level of 1 is the fastest compression method and
    produces the least compressions, while 9 is slowest and produces
    the most compression. Compression is turned off completely when
    level is 0.

For example, the array metadata below specifies that the compressor is
the Gzip codec configured with a compression level of 1::

    {
        "codecs": [{
            "name": "gzip",
            "configuration": {
                "level": 1
            }
        }],
    }


Format and algorithm
====================

This is a ``bytes -> bytes`` codec.

Encoding and decoding is performed using the algorithm defined in
[RFC1951]_.

Encoded data should conform to the Gzip file format [RFC1952]_.


References
==========

.. [RFC2119] S. Bradner. Key words for use in RFCs to Indicate
   Requirement Levels. March 1997. Best Current Practice. URL:
   https://tools.ietf.org/html/rfc2119

.. [RFC1951] P. Deutsch. DEFLATE Compressed Data Format Specification version
   1.3. Requirement Levels. May 1996. Informational. URL:
   https://tools.ietf.org/html/rfc1951

.. [RFC1952] P. Deutsch. GZIP file format specification version 4.3.
   Requirement Levels. May 1996. Informational. URL:
   https://tools.ietf.org/html/rfc1952


Change log
==========

No changes yet.
