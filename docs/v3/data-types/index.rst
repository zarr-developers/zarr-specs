.. _data-type-list:

==========
Data Types
==========

This document specifies the core data types of Zarr version 3. All
implementations SHOULD support every data type defined here.

Each data type is described by four properties:

Meaning
    What an element of the data type represents.

Values
    The set of values an element of the data type may take.

Identifier
    The JSON value used for the ``data_type`` field of array metadata to
    select the data type.

Element encoding
    The JSON encoding of a single element of the data type. This is the
    encoding used by the ``fill_value`` field of array metadata.

JSON schema
    A `JSON Schema <https://json-schema.org/>`_ (draft 2020-12) document for
    the data type. Each schema defines ``identifier`` and ``element`` under
    ``$defs``, and validates an object whose ``data_type`` and ``fill_value``
    members conform to them. Constraints that depend on values outside the
    schema, such as the length of a ``raw_bits`` element, are stated in the
    schema's ``description`` strings and are not machine-checked. The schema
    documents are informative; where a schema and the prose disagree, the
    prose is normative.

All of the data types defined here have a fixed size, in the sense that every
element requires the same number of bytes. Additional data types may be
defined as :ref:`extensions <extensions_section>`; registered data type
extensions can be found under
`zarr-extensions::data-types <https://github.com/zarr-developers/zarr-extensions/tree/main/data-types>`_.

.. _fill-value-list:

Fill values
-----------

The ``fill_value`` field of array metadata holds one element of the array's
data type, encoded as JSON. The permitted encodings depend on the data type
and are given in the *Element encoding* subsection of each data type below.

.. _float-element-encoding:

Floating point element encoding
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The IEEE 754 floating point data types (``float16``, ``float32``, ``float64``)
share the following element encoding, and the complex data types are built
from it. An element is encoded as either:

- A JSON number, which is rounded to the nearest representable value of the
  data type using the "round half to even" rule.

- A JSON string of one of the following forms:

  - ``"Infinity"``, denoting positive infinity;
  - ``"-Infinity"``, denoting negative infinity;
  - ``"NaN"``, denoting the not-a-number (NaN) value where the sign bit is 0
    (positive), the most significant bit (MSB) of the mantissa is 1, and all
    other bits of the mantissa are zero;
  - ``"0xYY..."``, a hexadecimal string specifying the bit pattern of the
    floating point number interpreted as an unsigned integer. The number of
    hexadecimal digits is fixed by the data type and is given in each data
    type's section. This representation is the only way to specify a NaN value
    other than the specific NaN value denoted by ``"NaN"``.

.. warning::

   While this NaN syntax is consistent with the syntax accepted by the C99
   ``strtod`` function, C99 leaves the meaning of the NaN payload string
   implementation defined, which may not match the Zarr definition.

Core data types
---------------

.. _dtype-bool:

bool
^^^^

Meaning
"""""""

A boolean value.

Values
""""""

``false`` or ``true``.

Identifier
""""""""""

The JSON string ``"bool"``.

Element encoding
""""""""""""""""

A JSON boolean (``false`` or ``true``).

JSON schema
""""""""""""

.. literalinclude:: schemas/bool.json
   :language: json

.. _dtype-int8:

int8
^^^^

Meaning
"""""""

A signed integer.

Values
""""""

Integers in ``[-2^7, 2^7-1]``.

Identifier
""""""""""

The JSON string ``"int8"``.

Element encoding
""""""""""""""""

A JSON number with no fraction or exponent part, within the range of the
data type.

JSON schema
""""""""""""

.. literalinclude:: schemas/int8.json
   :language: json

.. _dtype-int16:

int16
^^^^^

Meaning
"""""""

A signed integer.

Values
""""""

Integers in ``[-2^15, 2^15-1]``.

Identifier
""""""""""

The JSON string ``"int16"``.

Element encoding
""""""""""""""""

A JSON number with no fraction or exponent part, within the range of the
data type.

JSON schema
""""""""""""

.. literalinclude:: schemas/int16.json
   :language: json

.. _dtype-int32:

int32
^^^^^

Meaning
"""""""

A signed integer.

Values
""""""

Integers in ``[-2^31, 2^31-1]``.

Identifier
""""""""""

The JSON string ``"int32"``.

Element encoding
""""""""""""""""

A JSON number with no fraction or exponent part, within the range of the
data type.

JSON schema
""""""""""""

.. literalinclude:: schemas/int32.json
   :language: json

.. _dtype-int64:

int64
^^^^^

Meaning
"""""""

A signed integer.

Values
""""""

Integers in ``[-2^63, 2^63-1]``.

Identifier
""""""""""

The JSON string ``"int64"``.

Element encoding
""""""""""""""""

A JSON number with no fraction or exponent part, within the range of the
data type.

JSON schema
""""""""""""

.. literalinclude:: schemas/int64.json
   :language: json

.. _dtype-uint8:

uint8
^^^^^

Meaning
"""""""

An unsigned integer.

Values
""""""

Integers in ``[0, 2^8-1]``.

Identifier
""""""""""

The JSON string ``"uint8"``.

Element encoding
""""""""""""""""

A JSON number with no fraction or exponent part, within the range of the
data type.

JSON schema
""""""""""""

.. literalinclude:: schemas/uint8.json
   :language: json

.. _dtype-uint16:

uint16
^^^^^^

Meaning
"""""""

An unsigned integer.

Values
""""""

Integers in ``[0, 2^16-1]``.

Identifier
""""""""""

The JSON string ``"uint16"``.

Element encoding
""""""""""""""""

A JSON number with no fraction or exponent part, within the range of the
data type.

JSON schema
""""""""""""

.. literalinclude:: schemas/uint16.json
   :language: json

.. _dtype-uint32:

uint32
^^^^^^

Meaning
"""""""

An unsigned integer.

Values
""""""

Integers in ``[0, 2^32-1]``.

Identifier
""""""""""

The JSON string ``"uint32"``.

Element encoding
""""""""""""""""

A JSON number with no fraction or exponent part, within the range of the
data type.

JSON schema
""""""""""""

.. literalinclude:: schemas/uint32.json
   :language: json

.. _dtype-uint64:

uint64
^^^^^^

Meaning
"""""""

An unsigned integer.

Values
""""""

Integers in ``[0, 2^64-1]``.

Identifier
""""""""""

The JSON string ``"uint64"``.

Element encoding
""""""""""""""""

A JSON number with no fraction or exponent part, within the range of the
data type.

JSON schema
""""""""""""

.. literalinclude:: schemas/uint64.json
   :language: json

.. _dtype-float16:

float16
^^^^^^^

Meaning
"""""""

An IEEE 754 half-precision (binary16) floating point number: sign bit,
5 bits exponent, 10 bits mantissa.

Values
""""""

All values representable by IEEE 754 binary16, including positive and negative
zero, positive and negative infinity, and NaN values.

Identifier
""""""""""

The JSON string ``"float16"``.

Element encoding
""""""""""""""""

As specified in :ref:`float-element-encoding`. The hexadecimal string form has
exactly 4 hexadecimal digits, e.g. ``"0x7e00"`` is equivalent to ``"NaN"``.

JSON schema
""""""""""""

.. literalinclude:: schemas/float16.json
   :language: json

.. _dtype-float32:

float32
^^^^^^^

Meaning
"""""""

An IEEE 754 single-precision (binary32) floating point number: sign bit,
8 bits exponent, 23 bits mantissa.

Values
""""""

All values representable by IEEE 754 binary32, including positive and negative
zero, positive and negative infinity, and NaN values.

Identifier
""""""""""

The JSON string ``"float32"``.

Element encoding
""""""""""""""""

As specified in :ref:`float-element-encoding`. The hexadecimal string form has
exactly 8 hexadecimal digits, e.g. ``"0x7fc00000"`` is equivalent to
``"NaN"``.

JSON schema
""""""""""""

.. literalinclude:: schemas/float32.json
   :language: json

.. _dtype-float64:

float64
^^^^^^^

Meaning
"""""""

An IEEE 754 double-precision (binary64) floating point number: sign bit,
11 bits exponent, 52 bits mantissa.

Values
""""""

All values representable by IEEE 754 binary64, including positive and negative
zero, positive and negative infinity, and NaN values.

Identifier
""""""""""

The JSON string ``"float64"``.

Element encoding
""""""""""""""""

As specified in :ref:`float-element-encoding`. The hexadecimal string form has
exactly 16 hexadecimal digits, e.g. ``"0x7ff8000000000000"`` is equivalent to
``"NaN"``.

JSON schema
""""""""""""

.. literalinclude:: schemas/float64.json
   :language: json

.. _dtype-complex64:

complex64
^^^^^^^^^

Meaning
"""""""

A complex number whose real and imaginary components are each an IEEE 754
single-precision floating point number.

Values
""""""

All pairs of values representable by IEEE 754 binary32.

Identifier
""""""""""

The JSON string ``"complex64"``.

Element encoding
""""""""""""""""

A two-element JSON array specifying the real and imaginary components
respectively, where each component is encoded as specified for
:ref:`float32 <dtype-float32>`.

For example, ``[1, 2]`` indicates ``1 + 2i`` and ``["-Infinity", "NaN"]``
indicates a complex number with real component of -inf and imaginary component
of NaN.

JSON schema
""""""""""""

.. literalinclude:: schemas/complex64.json
   :language: json

.. _dtype-complex128:

complex128
^^^^^^^^^^

Meaning
"""""""

A complex number whose real and imaginary components are each an IEEE 754
double-precision floating point number.

Values
""""""

All pairs of values representable by IEEE 754 binary64.

Identifier
""""""""""

The JSON string ``"complex128"``.

Element encoding
""""""""""""""""

A two-element JSON array specifying the real and imaginary components
respectively, where each component is encoded as specified for
:ref:`float64 <dtype-float64>`.

JSON schema
""""""""""""

.. literalinclude:: schemas/complex128.json
   :language: json

.. _dtype-raw:

raw_bits
^^^^^^^^

Meaning
"""""""

A fixed-length sequence of raw bytes with no further interpretation. This is a
pass-through type: implementations MUST preserve the bytes of each element
exactly and MUST NOT reinterpret them, e.g. by applying a byte order.

Values
""""""

All byte sequences of length ``length_bits / 8``, where ``length_bits`` is
given by the identifier.

Identifier
""""""""""

A JSON object of the form::

    {
        "name": "raw_bits",
        "configuration": {
            "length_bits": <int>
        }
    }

The ``configuration`` object is required and has the following members:

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Required
     - Constraints
   * - ``length_bits``
     - JSON number (integer)
     - Yes
     - A positive integer divisible by 8, giving the size of each element in
       bits.

The ``configuration`` object is closed: it MUST NOT contain any members other
than those listed above.

For example, an element of 3 bytes is identified by::

    {"name": "raw_bits", "configuration": {"length_bits": 24}}

Legacy string identifier
~~~~~~~~~~~~~~~~~~~~~~~~

Earlier revisions of this specification identified this data type by the JSON
string ``"r<N>"``, where ``<N>`` is the decimal representation of
``length_bits``, e.g. ``"r24"``. This string is a legacy synonym for the
object form: ``"r24"`` is equivalent to
``{"name": "raw_bits", "configuration": {"length_bits": 24}}``.

Implementations MUST accept the legacy string form when reading array
metadata. Implementations SHOULD NOT write the legacy string form; the object
form is RECOMMENDED when writing.

.. note::

   The legacy string form is not a :ref:`short-hand name
   <extension-definition-short-hand-name>` in the sense of the extension
   definition, because it embeds the configuration in the string. It is a
   special case that exists only for this data type and for backwards
   compatibility. No other data type, core or extension, may define a string
   identifier that carries configuration.

Element encoding
""""""""""""""""

Either:

- A JSON array of integers with length equal to ``length_bits / 8``, where
  each integer is in the range ``[0, 255]`` and gives the value of the
  corresponding byte of the element, in order.

- A JSON string produced by applying base64 encoding (as specified in
  :rfc:`4648`, section 4, with padding) to the ``length_bits / 8`` bytes of
  the element.

For example, for ``length_bits`` equal to 24, the array ``[0, 1, 255]`` and
the string ``"AAH/"`` denote the same element.

JSON schema
""""""""""""

.. literalinclude:: schemas/raw_bits.json
   :language: json
