
.. _regulargrid-chunkgrid-v1:

======================================
 Regular grid chunk grid (version 1.0)
======================================

  **Editor's draft 26 July 2019**

Specification URI:
    https://zarr-specs.readthedocs.io/en/latest/v3/chunk-grids/regular-grid/v1.0.html
Corresponding ZEP:
    `ZEP0001 — Zarr specification version 3 <https://zarr.dev/zeps/draft/ZEP0001.html>`_
Issue tracking:
    `GitHub issues <https://github.com/zarr-developers/zarr-specs/labels/chunk-grid>`_
Suggest an edit for this spec:
    `GitHub editor <https://github.com/zarr-developers/zarr-specs/blob/main/docs/v3/chunk-grids/regular-grid/index.rst>`_

Copyright 2020-Present Zarr core development team. This work
is licensed under a `Creative Commons Attribution 3.0 Unported License
<https://creativecommons.org/licenses/by/3.0/>`_.

----

Abstract
========

A regular grid is a type of grid where an array is divided into chunks
such that each chunk is a hyperrectangle of the same shape. The
dimensionality of the grid is the same as the dimensionality of the
array. Each chunk in the grid can be addressed by a tuple of positive
integers (`k`, `j`, `i`, ...) corresponding to the indices of the
chunk along each dimension.

Description
===========

The origin element of a chunk has coordinates in the array space (`k` *
`dz`, `j` * `dy`, `i` * `dx`, ...) where (`dz`, `dy`, `dx`, ...) are
the chunk sizes along each dimension.
Thus the origin element of the chunk at grid index (0, 0, 0,
...) is at coordinate (0, 0, 0, ...) in the array space, i.e., the
grid is aligned with the origin of the array. If the length of any
array dimension is not perfectly divisible by the chunk length along
the same dimension, then the grid will overhang the edge of the array
space.

The shape of the chunk grid will be (ceil(`z` / `dz`), ceil(`y` /
`dy`), ceil(`x` / `dx`), ...)  where (`z`, `y`, `x`, ...) is the array
shape, "/" is the division operator and "ceil" is the ceiling
function. For example, if a 3 dimensional array has shape (10, 200,
3000), and has chunk shape (5, 20, 400), then the shape of the chunk
grid will be (2, 10, 8), meaning that there will be 2 chunks along the
first dimension, 10 along the second dimension, and 8 along the third
dimension.

.. list-table:: Regular Grid Example
    :header-rows: 1

    * - Array Shape
      - Chunk Shape
      - Chunk Grid Shape
      - Notes
    * - (10, 200, 3000)
      - (5, 20, 400)
      - (2, 10, 8)
      - The grid does overhang the edge of the array on the 3rd dimension.

An element of an array with coordinates (`c`, `b`, `a`, ...) will
occur within the chunk at grid index (`c` // `dz`, `b` // `dy`, `a` //
`dx`, ...), where "//" is the floor division operator. The element
will have coordinates (`c` % `dz`, `b` % `dy`, `a` % `dx`, ...) within
that chunk, where "%" is the modulo operator. For example, if a
3 dimensional array has shape (10, 200, 3000), and has chunk shape
(5, 20, 400), then the element of the array with coordinates (7, 150, 900)
is contained within the chunk at grid index (1, 7, 2) and has coordinates
(2, 10, 100) within that chunk.

The store key corresponding to a given grid cell is determined based on the
:ref:`array-metadata-chunk-key-encoding` member of the :ref:`array-metadata`.

Note that this specification does not consider the case where the
chunk grid and the array space are not aligned at the origin vertices
of the array and the chunk at grid index (0, 0, 0, ...). However,
extensions may define variations on the regular grid type
such that the grid indices may include negative integers, and the
origin element of the array may occur at an arbitrary position within
any chunk, which is required to allow arrays to be extended by an
arbitrary length in a "negative" direction along any dimension.

.. note:: Chunks at the border of an array always have the full chunk size, even when
   the array only covers parts of it. For example, having an array with ``"shape": [30, 30]`` and
   ``"chunk_shape": [16, 16]``, the chunk ``0,1`` would also contain unused values for the indices
   ``0-16, 30-31``. When writing such chunks it is recommended to use the current fill value
   for elements outside the bounds of the array.



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
