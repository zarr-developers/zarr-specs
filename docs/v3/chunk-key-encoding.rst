.. _chunk-key-encoding-list:

===================
Chunk Key Encodings
===================

The following core chunk key encodings are defined by the specification.
Being listed below does not imply that a chunk key encoding is
required to be implemented by implementations.

Core chunk key encodings
------------------------

The following encodings are defined:

``default``
^^^^^^^^^^^

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

``v2``
^^^^^^

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

Extensions
----------

Registered chunk grid extensions can be found under
`zarr-extensions::chunk-key-encodings <https://github.com/zarr-developers/zarr-extensions/tree/main/chunk-key-encodings>`_.
