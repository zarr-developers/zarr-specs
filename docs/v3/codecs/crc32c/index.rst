.. _crc32c-codec:

=====================
CRC32C checksum codec
=====================

Version:
    1.0
Specification URI:
    https://zarr-specs.readthedocs.io/en/latest/v3/codecs/crc32c/
Editors:
    * Jonathan Striebel (`@jstriebel <https://github.com/jstriebel>`_), Scalable Minds
    * Norman Rzepka (`@normanrz <https://github.com/normanrz>`_), Scalable Minds
    * Jeremy Maitin-Shepard (`@jbms <https://github.com/jbms>`_), Google
Corresponding ZEP:
    `ZEP0002 — Sharding codec <https://zarr.dev/zeps/accepted/ZEP0002.html>`_
Issue tracking:
    `GitHub issues <https://github.com/zarr-developers/zarr-specs/labels/codec>`_
Suggest an edit for this spec:
    `GitHub editor <https://github.com/zarr-developers/zarr-specs/blob/main/docs/v3/codecs/crc32c/index.rst>`_

Copyright 2022-Present `Zarr core development team
<https://github.com/orgs/zarr-developers/teams/core-devs>`_. This work
is licensed under a `Creative Commons Attribution 3.0 Unported License
<https://creativecommons.org/licenses/by/3.0/>`_.

----


Abstract
========

Defines an ``bytes -> bytes`` codec that appends a CRC32C checksum of the input bytestream.


Status of this document
=======================

ZEP0002 was accepted on November 1st, 2023 via https://github.com/zarr-developers/zarr-specs/issues/254.

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

The value of the ``name`` member in the codec object MUST be ``crc32c``.


Configuration parameters
========================

None.


Format and algorithm
====================

This is a ``bytes -> bytes`` codec.

The codec computes the CRC32C checksum as defined in [RFC3720]_ of the input
bytestream. The output bytestream is composed of the unchanged input byte 
stream with the appended checksum. The checksum is represented as a 32-bit
unsigned integer represented in little endian. 


References
==========

.. [RFC2119] S. Bradner. Key words for use in RFCs to Indicate
   Requirement Levels. March 1997. Best Current Practice. URL:
   https://tools.ietf.org/html/rfc2119

.. [RFC3720] J. Satran et al. Internet Small Computer Systems 
   Interface (iSCSI). April 2004. Proposed Standard. URL:
   https://tools.ietf.org/html/rfc3720


Change log
==========

No changes yet.
