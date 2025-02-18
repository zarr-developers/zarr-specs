.. _chunk-grid-list:

==========
Chunk Grid
==========

The following core chunk grids are defined by the maintainers of
the Zarr specification. Being listed below does not imply that a data type is
required to be implemented by implementations.

Regular grids
-------------

A regular grid is a type of grid where an array is divided into chunks
such that each chunk is a hyperrectangle of the same shape. The
dimensionality of the grid is the same as the dimensionality of the
array. Each chunk in the grid can be addressed by a tuple of positive
integers (`k`, `j`, `i`, ...) corresponding to the indices of the
chunk along each dimension.

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


Extensions
----------

Registered chunk grid extensions can be found under
`zarr-extensions::chunk-grids <https://github.com/zarr-developers/zarr-extensions/tree/main/chunk-grids>`_.
