==============
Codec registry
==============
------------------------------
Editor's Draft 21 October 2020
------------------------------

Specification URI:
    https://purl.org/zarr/specs/codecs
Issue tracking:
    `GitHub issues <https://github.com/zarr-developers/zarr-specs/labels/codec>`_
Suggest an edit for this spec:
    `GitHub editor <https://github.com/zarr-developers/zarr-specs/blob/master/docs/codecs.rst>`_

Copyright 2020 `Zarr core development team
<https://github.com/orgs/zarr-developers/teams/core-devs>`_. This work
is licensed under a `Creative Commons Attribution 3.0 Unported License
<https://creativecommons.org/licenses/by/3.0/>`_.

----


Abstract
========

This document defines codecs for use as compressors and/or filters as
part of a Zarr implementation.


Status of this documents
========================

This document is a **Work in Progress**. It may be updated, replaced
or obsoleted by other documents at any time. It is inappapropriate to
cite this document as other than work in progress.

Comments, questions or contributions to this document are very
welcome. Comments and questions should be raised via `GitHub issues                                           
<https://github.com/zarr-developers/zarr-specs/labels/codec>`_.

This document is maintained by the `Zarr core development team
<https://github.com/orgs/zarr-developers/teams/core-devs>`_.


Document conventions
====================

This document lists a collection of codecs. For each codec, the
following information is provided:

* A URI which can be used to uniquely identify the codec in Zarr array
  metadata.
* Any configuration parameters which can be set in Zarr array
  metadata.
* A definition of encoding/decoding algorithm and the encoded format,
  or a citation to an existing specification where this is defined.
* Any additional headers added to the encoded data.

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


Codecs
======

Gzip
----

Codec URI:
    https://purl.org/zarr/spec/codecs/gzip

    
Configuration parameters
~~~~~~~~~~~~~~~~~~~~~~~~

level:
    An integer from 0 to 9 which controls the speed and level of
    compression. A level of 1 is the fastest compression method and
    produces the least compressions, while 9 is slowest and produces
    the most compression. Compression is turned off completely when
    level is 0.

For example, the array metadata below specifies that the compressor is
the Gzip codec configured with a compression level of 1::

    {
        "compressor": {
            "codec": "https://purl.org/zarr/spec/codecs/gzip",
            "configuration": {                                                                                
                "level": 1                                                                                    
            }
        },
    }

    
Format and algorithm
~~~~~~~~~~~~~~~~~~~~

Encoding and decoding is performed using the algorithm defined in
[RFC1951]_.

Encoded data should conform to the Gzip file format [RFC1952]_.


Blosc
-----

Codec URI:
    https://purl.org/zarr/spec/codecs/blosc

    
Configuration parameters
~~~~~~~~~~~~~~~~~~~~~~~~

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
    An integer value in the set {0, 1, 2, -1} indicating the way
    bytes or bits are rearranged, which can lead to faster
    and/or greater compression. A value of 1
    indicates that byte-wise shuffling is performed prior to
    compression. A value of 2 indicates the bit-wise shuffling is
    performed prior to compression. If a value of -1 is given,
    then default shuffling is used: bit-wise shuffling for buffers
    with item size of 1 byte, byte-wise shuffling otherwise.
    Shuffling is turned off completely when the value is 0.

blocksize:
    An integer giving the size in bytes of blocks into which a
    buffer is divided before compression.

For example, the array metadata document below specifies that the
compressor is the Blosc codec configured with a compression level of
1, byte-wise shuffling, the ``lz4`` compression algorithm and the
default block size::

    {
        "compressor": {
            "codec": "https://purl.org/zarr/spec/codecs/blosc",
            "configuration": {
                "cname": "lz4",
                "clevel": 1,
                "shuffle": 1,
                "blocksize": 0
            }
        },
    }


Format and algorithm
~~~~~~~~~~~~~~~~~~~~

Blosc is a meta-compressor, which divides an input buffer into blocks,
then applies an internal compression algorithm to each block, then
packs the encoded blocks together into a single output buffer with a
header. The format of the encoded buffer is defined in [BLOSC]_. The
reference implementation is provided by the `c-blosc library
<https://github.com/Blosc/c-blosc>`_.


Deprecated codecs
=================

There are no deprecated codecs at this time.


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

.. [BLOSC] F. Alted. Blosc Chunk Format. URL:
   https://github.com/Blosc/c-blosc/blob/master/README_CHUNK_FORMAT.rst


Change log
==========

Editor's Draft 21 October 2020
------------------------------

* Added Gzip codec.
* Added Blosc codec.
