
.. _regular-chunkgrid:

==================
Regular chunk grid
==================

Version:
    1.1
Specification URI:
    https://zarr-specs.readthedocs.io/en/latest/v3/chunk-grids/regular-grid/
Corresponding ZEP:
    `ZEP0001 — Zarr specification version 3 <https://zarr.dev/zeps/draft/ZEP0001.html>`_;
    `ZEP0012 — Explicit array bounds <https://zarr.dev/zeps/draft/ZEP0012.html>`_ (negative grid indices, version 1.1)
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
array. Each chunk in the grid can be addressed by a tuple of
integers (`k`, `j`, `i`, ...) corresponding to the indices of the
chunk along each dimension, which may be negative.

Description
===========

The origin element of a chunk has coordinates in the array space (`k` *
`dz`, `j` * `dy`, `i` * `dx`, ...) where (`dz`, `dy`, `dx`, ...) are
the chunk sizes along each dimension. Chunk sizes must be greater than zero.
Thus the origin element of the chunk at grid index (0, 0, 0,
...) is at coordinate (0, 0, 0, ...) in the array space, i.e., the
grid is aligned with the origin of the array space, and extends in both
directions from it.
Where the bounds of the array along a dimension do not fall on chunk
boundaries, the grid overhangs the edge of the array space: the first
chunk along that dimension may begin before the first element, and the
last may end after the last element. Positions of such a chunk outside
the bounds of the array are not elements of the array, and writers SHOULD
store the fill value in them.

Along a dimension with bounds [`start`, `stop`) (the array's ``inclusive_min``
and ``exclusive_max`` entries for that dimension) and chunk size `d`, the
grid runs from grid index floor(`start` / `d`) through
floor((`stop` - 1) / `d`) when `stop` > `start`, and has no chunks
when the dimension has length 0. For an array whose metadata gives a
``shape``, the shape of the chunk grid is (ceil(`z` /
`dz`), ceil(`y` / `dy`), ceil(`x` / `dx`), ...)  where (`z`, `y`, `x`, ...)
is the array shape, "/" is the division operator and "ceil" is the ceiling
function. For example, if a 3 dimensional array has shape (10, 200,
3000), and has chunk shape (5, 20, 400), then the shape of the chunk
grid will be (2, 10, 8), meaning that there will be 2 chunks along the
first dimension, 10 along the second dimension, and 8 along the third
dimension.

.. list-table:: Regular Grid Example
    :header-rows: 1

    * - Array extent
      - Chunk Shape
      - Chunk Grid Shape
      - Notes
    * - (10, 200, 3000)
      - (5, 20, 400)
      - (2, 10, 8)
      - The grid does overhang the edge of the array on the 3rd dimension.
    * - bounds [-3, 7), [0, 200), [0, 3000)
      - (5, 20, 400)
      - (3, 10, 8)
      - Grid indices run from -1 to 1 on the 1st dimension; the first chunk
        overhangs the array by 2 elements and the last by 3.

An element of an array with coordinates (`c`, `b`, `a`, ...) will
occur within the chunk at grid index (`c` // `dz`, `b` // `dy`, `a` //
`dx`, ...), where "//" is the floor division operator, rounding toward
negative infinity. The element will be at position (`c` % `dz`, `b` % `dy`,
`a` % `dx`, ...) within that chunk, where "%" is the modulo operator whose
result takes the sign of the divisor, so that both are well defined for
negative coordinates.
For example, if a 3 dimensional array has shape (10, 200, 3000), and has
chunk shape (5, 20, 400), then the element of the array with coordinates
(7, 150, 900) is contained within the chunk at grid index (1, 7, 2) and is at
position (2, 10, 100) within that chunk. With bounds [-3, 7) along the
first dimension, the element with coordinate -3 along that dimension is in
the chunk with grid index -1, at position 2 within it.

The store key corresponding to a given grid cell is determined based on the
:ref:`array-metadata-chunk-key-encoding` member of the :ref:`array-metadata`.

Configuration
-------------

``chunk_shape``
    Required. An array of integers, one per dimension of the array, giving
    the chunk size along each dimension. Each must be at least 1.

Lowering or raising ``inclusive_min`` in the array's :ref:`bounds
<array-metadata-bounds>` along a dimension grows or shrinks the array before
its first element without changing the grid index, and so the store key, of
any existing chunk.

This specification does not consider the case where the chunk at grid index
(0, 0, 0, ...) begins at a coordinate other than (0, 0, 0, ...). Extensions
may define grids that wrap this one and shift it; see the `chunk grids in the
extensions registry <https://github.com/zarr-developers/zarr-extensions/tree/main/chunk-grids>`_.

.. note:: Chunks at the border of an array always have the full chunk size, even when
   the array only covers parts of it. For example, having an array with ``"shape": [30, 30]`` and
   ``"chunk_shape": [16, 16]``, the chunk ``0,1`` would also contain unused values for the indices
   ``0-16, 30-31``. Likewise, with
   ``"bounds": {"inclusive_min": [-3, 0], "exclusive_max": [27, 30]}`` the chunk ``-1,0`` covers
   coordinates -16 to -1 along the first dimension, of which only -3 to -1 are elements of the
   array. When writing such chunks it is recommended to use the current fill value
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
