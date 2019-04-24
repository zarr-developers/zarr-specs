Spec development process
========================

This document defines and provides a guide to the development process
for specification documents ("specs") within the zarr-specs
repository.


Introduction
------------

The Zarr project is maintained by an open community of developers and
scientists, working primarily via GitHub. The spec development process
is intended to be open and inclusive, enabling anyone to comment and
contribute, and allowing for the community to grow or change without
blocking spec development or leaving anyone out of the decision
process.

There are four different types of spec:

* **Core protocol** - Defines the core protocol that all Zarr
  implementations support.

* **Protocol extensions** - Multiple specs, each of which defines an
  extension to the core protocol that may not be supported by all
  Zarr implementations.

* **Stores** - Multiple specs, each of which defines a concrete
  storage mechanism for Zarr data, such as file system, zip file or
  cloud object storage.

* **Codecs** - Multiple specs, each of which defines a codec that can
  be used within a pipeline for encoding and decoding data chunks,
  e.g., compressors or filters.

These specs have been decoupled to allow for some flexibility in
developing new specs. For example, it is possible to propose and
develop a new storage spec, or a new codec spec, without requiring any
changes to the core protocol.

Please note that there are slightly different processes for each of
these different spec types, described in more detail below.


Making proposals
----------------

New proposals are made by raising an issue on the zarr-specs GitHub
repository.

If you have an idea for a new protocol feature, but you don't yet know
or have any feeling about whether it should become part of the core
protocol or a protocol extension, please raise an issue and prefix the
issue title with the words **"Protocol proposal:"**.

If you would like to propose a new codec spec, please raise an issue and
prefix the title with **"Codec proposal:"**.

If you would like to propose a new storage spec, please raise an issue
and prefix the title with **"Store proposal:"**.

In general, it is good to make a proposal issue first, before
submitting a PR with any new or revised spec documents. Raising an
issue allows room to discuss scope and clarify ideas, and also guage
support and interest from the community.


Core protocol
-------------

The Zarr core protocol spec defines metadata formats, abstract
interfaces, and other protocol concepts which are central to the
implementation of systems that can read and write Zarr data. The
intention is that this spec should only contain protocol features that
**all** actively-maintained Zarr implementations agree to
support. Because of this, the process for developing the core protocol
is slightly different from other specs.

Versioning
~~~~~~~~~~

The Zarr core protocol spec is versioned using a [major].[minor]
versioning scheme. The spec documents live in the zarr-specs GitHub
repository at the location ``docs/protocol/core/v[major].[minor].rst``.

A new major version of the core protocol spec can include change which
are not backwards-compatible, in the sense that implementations of
previous major protocol versions would not correctly interpret data
written using the new protocol version, and therefore should not
attempt to read the data.

A new minor version of the core protocol spec can only include new
features which are backwards-compatible, in the sense that they can
safely be ignored by implementations of any previous minor version of
the core protocol within the same major version series. I.e., all
implementations of the same major version of the core protocol should
be interoperable, in the sense that data written by any one
implementation can be read correctly by any other implementation.

Process
~~~~~~~

TODO how do we decide to start work on a new major version of the core
protocol?

TODO how do we decide to start work on a new minor version of the core
protocol?

TODO once we have consensus to start work on a new version, what's the
process? Expect it will be based around someone making a PR, but any
constraints on who can make a PR? Do we need to nominate an editor or
editors, or can it happen organically?

TODO how do we transition from work in progress to stable? I.e., How
do we decide work is done? Any formal requests for comments at any
stage? What is role of @zarr-developers/core-devs? For core protocol,
we need explicit approval from all implementers?

TODO how do we indicate a spec is stable? How do we track changes to
fix errors etc.?

The act of merging a PR into the master branch transitions the spec to
the STABLE state. Before merging, the document should be edited to
include a message indicating that it is "STABLE". Once a spec has been
merged into master, further PRs can be made to fix errors, improve
clarity or add further explanation, but it cannot be changed in any
way that affects scope or meaning. Each spec should include a change
log to record a history of any changes made after it was merged into
master.


Protocol extensions
-------------------

TODO


Codecs
------

TODO


Stores
------

TODO
