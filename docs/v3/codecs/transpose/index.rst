.. _transpose-codec-v1:

==============================
 Transpose codec (version 1.0)
==============================

  **Editor's draft 26 July 2019**

Specification URI:
    https://zarr-specs.readthedocs.io/en/latest/v3/codecs/transpose/v1.0.html
Corresponding ZEP:
    `ZEP0001 — Zarr specification version 3 <https://zarr.dev/zeps/draft/ZEP0001.html>`_
Issue tracking:
    `GitHub issues <https://github.com/zarr-developers/zarr-specs/labels/codec>`_
Suggest an edit for this spec:
    `GitHub editor <https://github.com/zarr-developers/zarr-specs/blob/main/docs/v3/codecs/transpose/index.rst>`_

Copyright 2020-Present Zarr core development team. This work
is licensed under a `Creative Commons Attribution 3.0 Unported License
<https://creativecommons.org/licenses/by/3.0/>`_.

----


Abstract
========

Defines an ``array -> array`` codec that permutes the dimensions of the chunk
array.


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

The value of the ``name`` member in the codec object MUST be ``transpose``.


Configuration parameters
========================

order:
    Required.  Must be an array of integers specifying a permutation of ``0``, ``1``, ...,
    `n-1``, where ``n`` is the number of dimensions in the decoded chunk
    representation provided as input to this codec.

Format and algorithm
====================

This is an ``array -> array`` codec.

Given a chunk array ``A`` with shape ``A_shape`` as the decoded representation,
the encoded representation is an array ``B`` with the same data type as ``A``
and shape ``B_shape``, where:

- ``B_shape[i] = A_shape[order[i]]`` for all dimension indices ``i``, and
- ``B[B_pos] = A[A_pos]``, where ``B_pos[i] = A_pos[order[i]]``, for all chunk
  positions ``A_pos`` and dimension indices ``i``.

.. note::

   Implementations of this codec may simply construct a virtual view that
   represents the transposed result, and avoid physically transposing the
   in-memory representation when possible.

References
==========

.. [RFC2119] S. Bradner. Key words for use in RFCs to Indicate
   Requirement Levels. March 1997. Best Current Practice. URL:
   https://tools.ietf.org/html/rfc2119


Change log
==========

Changes after acceptance of ZEP 1
---------------------------------

The ``order`` configuration parameter no longer supports the constants ``"C"``
or ``"F"`` and must instead always be specified as an explicit permutation.
