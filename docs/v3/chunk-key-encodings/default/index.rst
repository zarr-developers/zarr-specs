.. _default-chunkkeyencoding:

==========================
Default chunk key encoding
==========================

Version:
    1.0
Specification URI:
    https://zarr-specs.readthedocs.io/en/latest/v3/chunk-key-encodings/default/
Corresponding ZEP:
    `ZEP0001 — Zarr specification version 3 <https://zarr.dev/zeps/draft/ZEP0001.html>`_
Issue tracking:
    `GitHub issues <https://github.com/zarr-developers/zarr-specs/labels/chunk-grid>`_
Suggest an edit for this spec:
    `GitHub editor <https://github.com/zarr-developers/zarr-specs/blob/main/docs/v3/chunk-key-encodings/default/index.rst>`_

Copyright 2020-Present Zarr core development team. This work
is licensed under a `Creative Commons Attribution 3.0 Unported License
<https://creativecommons.org/licenses/by/3.0/>`_.

----

Description
===========

The ``configuration`` object may contain one optional member,
``separator``, which must be either ``"/"`` or ``"."``.  If not specified,
``separator`` defaults to ``"/"``.

The key for a chunk with grid index (``k``, ``j``, ``i``, ...) is
formed by taking the initial prefix ``c``, and appending for each dimension:

- the ``separator`` character, followed by,

- the ASCII decimal string representation of the chunk index within that dimension.

For example, in a 3 dimensional array, with a separator of ``/`` the identifier
for the chunk at grid index (1, 23, 45) is the string ``"c/1/23/45"``.  With a
separator of ``.``, the identifier is the string ``"c.1.23.45"``. The initial prefix 
``c`` ensures that metadata documents and chunks have separate prefixes.

.. note:: A main difference with spec v2 is that the default chunk separator
    changed from ``.`` to ``/``, as in N5.  This decreases the maximum number of
    items in hierarchical stores like directory stores.

.. note:: Arrays may have 0 dimensions (when for example representing scalars),
    in which case the coordinate of a chunk is the empty tuple, and the chunk key
    will consist of the string ``c``.


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
