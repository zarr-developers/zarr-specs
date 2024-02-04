===========
Conventions
===========

Why Conventions?
~~~~~~~~~~~~~~~~

Zarr Conventions provide a mechanism to standardize metadata and layout of Zarr data
in order to meet domain-specific application needs without changes to the
core Zarr data model and specification, and without specification extensions.

Conventions must fit completely within the Zarr data / metadata model of groups, arrays, and attributes thereof, requiring
no changes or extension to the specification.
A Zarr implementation itself should not even be aware of the existence of the convention.
The line between a convention and an extension may be blurry in some cases.
The key distinction lies in the implementation: the responsibility for interpreting a *convention* relies completely with downstream,
domain-specific software, while an *extension* must be handled by the Zarr implementation itself.
A good rule of thumb is that a user should be able to safely ignore the convention and still be able to interact with the data via the core Zarr library,
even if some domain-specific context or functionality is missing.
If the data are completely meaningless or unintelligible without the convention, then it should be an extension instead.

Conventions can also help users switch between different storage libraries more flexibly.
Since Zarr and HDF5 implement nearly identical data models, a single convention can be applied to both formats.
This allows downstream software to maintain better separation of concerns between storage and domain-specific logic.

Conventions are modular and composable. A single group or array can conform to multiple conventions.


Describing Conventions
~~~~~~~~~~~~~~~~~~~~~~

Conventions Document
--------------------

Conventions are described by a *convention document*.
TODO: say more about the structure and format of this document

Explicit Conventions
--------------------

The preferred way of identifying the presence of a convention in a Zarr group or array is via the attribute `zarr_conventions`.
This attribute must be an array of strings; each string is an identifier for the convention.
Multiple conventions may be present.

For example, a group metadata JSON document with conventions present might look like this

.. code-block:: json

   {
      "zarr_format": 3,
      "node_type": "group",
      "attributes": {
         "zarr_conventions": ["units-v1", "foo],
      }
   }

where `units-v1` and `bar` are the convention identifiers.


Legacy Conventions
------------------

A legacy convention is a convention already in use that predates this ZEP.
Data conforming to legacy conventions will not have the `zarr_conventions` attribute.
The conventions document must therefore specify how software can identify the presence of the convention through a series of rules or tests.

For those comfortable with the terminology, legacy conventions can be thought of as a "conformance class" and a corresponding "conformance test".

Namespacing
-----------

Conventions may choose to store their attributes on a specific namespace.
This ZEP does not specify how namespacing works; that is up to the convention.
For example, the namespace may be specified as a prefix on attributes, e.g.

.. code-block:: json

   {
      "attributes": {"units-v1:units": "m^2"}
   }


or via a nested JSON object, e.g.

.. code-block:: json

   {
      "attributes": {"units-v1": {"units: "m^2"}}
   }

The use of namespacing is optional and is up to the convention to decide.


Proposing Conventions
~~~~~~~~~~~~~~~~~~~~~

New conventions are proposed via a pull-request to the `zarr-specs` repo which adds a new conventions document.
If the convention is already documented elsewhere, the convention document can just contain a reference to the external documentation.
The author of the PR is expected to convene the relevant domain community to review and discuss the ZEP.
This includes posting a link to the PR on relevant forums, mailing lists, and social-media platforms.

The goal of the discussion is to reach a _consensus_ among the domain community regarding the convention.
The Zarr steering council, together with the PR author, will determine if a consensus has been reached, at which point the PR
can be merged and the convention published on the website.
If a consensus cannot be reached, the steering council may still decide to publish the convention, accompanied by a
disclaimer that it is not a consensus, and noting any objections that were raised during the discussion.

It is also possible that multiple, competing conventions exist in the same domain. While not ideal, it's not up to
the Zarr community to resolve such domain-specific debates.
These conventions should still be documented in a central location, which hopefully helps move towards alignment.

Conventions should be versioned using incremental integers, starting from 1.
Or, if the community already has an existing versioning system for their convention, that can be used instead (e.g. CF conventions).
The community is free to update their convention via a pull request using the same consensus process described above.
The conventions document should include a changelog.
Details of how to manage changes and backwards compatibility are left to the domain community.


Existing Conventions
~~~~~~~~~~~~~~~~~~~~


This page lists the Zarr conventions. The proposal to formalize the conventions is introduced in `ZEP0004 <https://zarr.dev/zeps/draft/ZEP0004.html>`_.

Some of the widely used conventions are:

- `GDAL <https://gdal.org/drivers/raster/zarr.html>`_
- `OME-NGFF <https://ngff.openmicroscopy.org/>`_
- `NCZarr <https://docs.unidata.ucar.edu/nug/current/nczarr_head.html>`_
- `Xarray <https://docs.xarray.dev/en/stable/internals/zarr-encoding-spec.html>`_

Any new conventions accepted by the `ZEP <https://zarr.dev/zeps/active/ZEP0000.html>`_ process will be listed here.

.. toctree::
   :glob:
   :maxdepth: 1
   :titlesonly:
   :caption: Contents:

   xarray

