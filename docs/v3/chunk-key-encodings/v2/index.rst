.. _v2-chunkkeyencoding-v1:

=========================================
 v2 chunk key encoding (version 1.0)
=========================================

  **Editor's draft 26 July 2019**

Specification URI:
    https://zarr-specs.readthedocs.io/en/latest/v3/chunk-key-encodings/v2/v1.0.html
Corresponding ZEP:
    `ZEP0001 — Zarr specification version 3 <https://zarr.dev/zeps/draft/ZEP0001.html>`_
Issue tracking:
    `GitHub issues <https://github.com/zarr-developers/zarr-specs/labels/chunk-grid>`_
Suggest an edit for this spec:
    `GitHub editor <https://github.com/zarr-developers/zarr-specs/blob/main/docs/v3/chunk-key-encodings/v2/index.rst>`_

Copyright 2020-Present Zarr core development team. This work
is licensed under a `Creative Commons Attribution 3.0 Unported License
<https://creativecommons.org/licenses/by/3.0/>`_.

----

Description
===========

The ``configuration`` object may contain one optional member,
``separator``, which must be either ``"/"`` or ``"."``.  If not specified,
``separator`` defaults to ``"."``.

The identifier for chunk with at least one dimension is formed by
concatenating for each dimension:

 - the ASCII decimal string representation of the chunk index within that
   dimension, followed by

 - the ``separator`` character, except that it is omitted for the last
   dimension.

For example, in a 3 dimensional array, with a separator of ``.`` the identifier
for the chunk at grid index (1, 23, 45) is the string ``"1.23.45"``.  With a
separator of ``/``, the identifier is the string ``"1/23/45"``.

For chunk grids with 0 dimensions, the single chunk has the key ``"0"``.

.. note::

    This encoding is intended only to allow existing v2 arrays to be
    converted to v3 without having to rename chunks.  It is not recommended
    to be used when writing new arrays.


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
