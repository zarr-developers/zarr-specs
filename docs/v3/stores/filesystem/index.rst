.. _file-system-store-v1:

=================================
 File system store (version 1.0)
=================================

Specification URI:
    https://zarr-specs.readthedocs.io/en/latest/v3/stores/filesystem/
Corresponding ZEP:
    `ZEP0001 — Zarr specification version 3 <https://zarr.dev/zeps/accepted/ZEP0001.html>`_
Issue tracking:
    `GitHub issues <https://github.com/zarr-developers/zarr-specs/labels/stores-filesystem-v1.0>`_
Suggest an edit for this spec:
    `GitHub editor <https://github.com/zarr-developers/zarr-specs/blob/main/docs/v3/stores/filesystem/index.rst>`_

Copyright 2019-Present Zarr core development team. This work is
licensed under a `Creative Commons Attribution 3.0 Unported License
<https://creativecommons.org/licenses/by/3.0/>`_.

----


Abstract
========

This specification defines an implementation of the Zarr abstract
store API using a file system.


Status of this document
=======================

ZEP0001 was accepted on May 15th, 2023 via https://github.com/zarr-developers/zarr-specs/issues/227.


Notes about design decisions for the native File System Store 
=============================================================

The original file system store is designed for simplicity and easy manipulation
and transfer  by external tools not aware of the store structure. In particular,
tools like ``gsutil`` can be use to transfer a local directory store to cloud
base storage, hence the keys choices will be conserved.


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


Native storage operations
=========================

Here we consider a file system to be any system comprised of files and
directories, where:

* Each file has a name (sequence of characters) and contents
  (sequence of bytes).

* Each directory has a name (sequence of characters) and children (set
  of zero or more files and/or directories).

* Each file or directory can be addressed by a path, comprised of its
  name and the names of all ancestor directories, which uniquely
  identifies it within the file system.

… and where the following native operations are supported:

* Create a file.

* Write the contents of a file.

* Read the contents of a file.

* Delete a file.

* Create a directory.

* List the children of a directory, returning the name and type (file
  or directory) of each child.

* Delete a directory.


Key translation
===============

The Zarr store interface is defined in terms of `keys` and `values`,
where a `key` is a sequence of characters and a `value` is a sequence
of bytes. A file system store translates keys into file system
paths. This translation assumes that the store has been defined
relative to a base directory. The translation is as follows:

* Replace any forward slash characters ('/') in the key with the
  native directory separator for the file system.

* Join the result to the base directory path, using the native
  directory separator.

For example, if the file system is a POSIX file system, and the base
directory path is "/data", then the key "foo/bar" is translated to the
file system path "/data/foo/bar".

For example, if the file system is a Windows file system, and the base
directory path is "C:\\data", then the key "foo/bar" is translated to
the file system path "C:\\data\\foo\\bar".

When returning information about available keys, a file system store
performs the reverse translation from file system paths to keys. This
translation is as follows:

* Replace any native directory separator characters with the forward
  slash character.

* Strip the base directory path from the beginning of the path.

For example, if the file system is a POSIX file system, and the base
directory path is "/data", then the file system path "/data/foo/bar"
is translated to the key "foo/bar".

For example, if the file system is a Windows file system, and the base
directory path is "C:\\data", then the file system path
"C:\\data\\foo\\bar" is translated to the key "foo/bar".


Store API implementation
========================

The section below defines an implementation of the Zarr
:ref:`abstract-store-interface` in terms of the native operations of this
storage system. Below ``fspath_to_key()`` is a function that
translates file system paths to store keys, and ``key_to_fspath()`` is
a function that translates store keys to file system paths, as defined
in the section above.

* ``get(key) -> value`` : Read and return the contents of the file at
  file system path ``key_to_fspath(key)``.

* ``set(key, value)`` : Write ``value`` as the contents of the file at
  file system path ``key_to_fspath(key)``.

* ``delete(key)`` : Delete the file or directory at file system path
  ``key_to_fspath(key)``.

* ``list()`` : Recursively walk the file system from the base
  directory, returning an iterator over keys obtained by calling
  ``fspath_to_key(fp)`` for each descendant file path ``fp``.

* ``list_prefix(prefix)`` : Obtain a file system path by calling
  ``key_to_fspath(prefix)``. If the result is a directory path,
  recursively walk the file system from this directory, returning an
  iterator over keys obtained by calling ``fspath_to_key(fp)`` for
  each descendant file path ``fp``.

* ``list_dir(prefix)`` : Obtain a file system path by calling
  ``key_to_fspath(prefix)``. If the result is a directory path, list
  the directory children. Return a set of keys obtained by calling
  ``fspath_to_key(fp)`` for each child file path ``fp``, and a set of
  prefixes obtained by calling ``fspath_to_key(dp)`` for each child
  directory path ``dp``.


Canonical URI
=============

The canonical URI format for this store follows the file URI scheme of the base
directory path, as defined in [RFC8089]_. For a Windows base directory path
"c:\\my data" the canonical URI would be "file:///c:/my%20data", for a Posix
base directory "/my data" it would be"file:///my%20data".

When expecting a URI string, but no scheme is present, implementations may
assume a filesystem store with the (supposedly URI) string as the base directory
path.


Store limitations
=================

The following limitations for this store are know:

* `260 characters path length limit in Windows <https://learn.microsoft.com/en-us/windows/win32/fileio/maximum-file-path-limitation>`_
* `Windows paths are case-insensitive by default <https://learn.microsoft.com/en-us/windows/win32/fileio/naming-a-file#naming-conventions>`_
* `MacOS paths are case-insensitive by default <https://support.apple.com/guide/disk-utility/file-system-formats-dsku19ed921c/mac>`_


References
==========

.. [RFC2119] S. Bradner. Key words for use in RFCs to Indicate
   Requirement Levels. March 1997. Best Current Practice. URL:
   https://tools.ietf.org/html/rfc2119

.. [RFC8089] M. Kerwin. The "file" URI Scheme. February 2017. Proposed Standard.
   URL: https://tools.ietf.org/html/rfc8089


Change log
==========

No changes yet.
