===========================
 Blosc codec (version 1.0)
===========================

  **Editor's draft 26 July 2019**

Specification URI:
    https://zarr-specs.readthedocs.io/en/latest/v3/codecs/blosc/
Corresponding ZEP:
    `ZEP0001 — Zarr specification version 3 <https://zarr.dev/zeps/accepted/ZEP0001.html>`_
Issue tracking:
    `GitHub issues <https://github.com/zarr-developers/zarr-specs/labels/codec>`_
Suggest an edit for this spec:
    `GitHub editor <https://github.com/zarr-developers/zarr-specs/blob/main/docs/v3/codecs/blosc/index.rst>`_

Copyright 2020-Present Zarr core development team. This work
is licensed under a `Creative Commons Attribution 3.0 Unported License
<https://creativecommons.org/licenses/by/3.0/>`_.

----


Abstract
========

Defines a ``bytes -> bytes`` codec that uses the blosc container format.


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

The value of the ``name`` member in the codec object MUST be ``blosc``.


Configuration parameters
========================

cname:
    A string identifying the internal compression algorithm to be
    used. At the time of writing, the following values are supported
    by the c-blosc library: "lz4", "lz4hc", "blosclz", "zstd",
    "snappy", "zlib".
    
clevel:
    An integer from 0 to 9 which controls the speed and level of
    compression. A level of 1 is the fastest compression method and
    produces the least compressions, while 9 is slowest and produces
    the most compression. Compression is turned off completely when
    level is 0.

shuffle:
    Specifies the type of shuffling to perform, if any, prior to compression.
    Must be one of:

    - ``"noshuffle"``, to indicate no shuffling;
    - ``"shuffle"``, to indicate byte-wise shuffling;
    - ``"bitshuffle"``, to indicate bit-wise shuffling.

    Zarr implementations MAY provide users an option to choose a shuffle mode
    automatically based on the typesize or other information, but MUST record in
    the metadata the mode that is chosen.

typesize:
    Positive integer specifying the stride in bytes over which shuffling is
    performed.  Required unless ``shuffle`` is ``"noshuffle"``, in which case the value
    is ignored.

    Zarr implementations MAY allow users to leave this unspecified and have the
    implementation choose a value automatically based on the array data type and
    previous codecs in the chain, but MUST record in the metadata the value that
    is chosen.

blocksize:
    An integer giving the size in bytes of blocks into which a
    buffer is divided before compression. A value of 0
    indicates that an automatic size will be used.

For example, the array metadata document below specifies that the compressor is
the Blosc codec configured with a compression level of 1, byte-wise shuffling
with a stride of 4, the ``lz4`` compression algorithm and the default block
size::

    {
        "codecs": [{
            "name": "blosc",
            "configuration": {
                "cname": "lz4",
                "clevel": 1,
                "shuffle": "shuffle",
                "typesize": 4,
                "blocksize": 0
            }
        }],
    }


Format and algorithm
====================

This is a ``bytes -> bytes`` codec.

Blosc is a meta-compressor, which divides an input buffer into blocks,
then applies an internal compression algorithm to each block, then
packs the encoded blocks together into a single output buffer with a
header. The format of the encoded buffer is defined in [BLOSC]_. The
reference implementation is provided by the `c-blosc library
<https://github.com/Blosc/c-blosc>`_.


Comparison to Zarr v2
=====================

While the binary format is identical, the JSON metadata differs from that used
by the Zarr v2 ``blosc`` codec in the following ways:

- The `shuffle` mode is now specified more clearly as `noshuffle` (0 in Zarr v2),
  `"bitshuffle"` (2 in Zarr v2), or `"shuffle"` (1 in Zarr v2).  Using these constants
  rather than numbers makes it much easier to know what shuffle mode will be
  used from manual inspection of the metadata.

- When shuffling is enabled, the `typesize` must now be specified explicitly in
  the metadata, rather than determined implicitly from the input data.  This
  allows Blosc to function as a pure "bytes -> bytes" codec rather than an
  "array -> bytes" codec.

- There is no option to choose between bit-wise and byte-wise shuffling
  automatically, as supported in Zarr v2 via a `shuffle` value of `-1`.

References
==========

.. [RFC2119] S. Bradner. Key words for use in RFCs to Indicate
   Requirement Levels. March 1997. Best Current Practice. URL:
   https://tools.ietf.org/html/rfc2119

.. [BLOSC] F. Alted. Blosc Chunk Format. URL:
   https://github.com/Blosc/c-blosc/blob/HEAD/README_CHUNK_FORMAT.rst


Change log
==========

No changes yet.
