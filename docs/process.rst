Specification development process
=================================

This document defines development processes for specification
documents ("specs") within the zarr-specs repository. 

General processes for all specs
-------------------------------

The current processes for development of all specs are intended to be
lightweight, built around GitHub, and built around the current
community, which is a loose collaboration of developers and scientists
with limited and variable bandwidth. The processes are also intended
to be open and enable anyone to comment and contribute, to allow for
the community to grow or change without blocking spec development or
leaving anyone out of the decision process.

A spec can be in one of three states:

  * NEW SPEC PROPOSAL
  * WORK IN PROGRESS
  * STABLE

A NEW SPEC PROPOSAL is made by raising an issue on the zarr-specs
repo, prefixing the issue title with "NEW SPEC PROPOSAL:". The issue
should state where the new spec file will live within the zarr-specs
repo file structure. The issue should also state what the scope of the
new spec will be, and any relevant technical details.

If there are no objections to a NEW SPEC PROPOSAL within one month,
then a pull request (PR) against the master branch adding the new spec
file is welcome. The action of making a PR with a new spec file
transitions the spec to the WORK IN PROGRESS state. The new spec file
should include a message clearly indicating that it is "WORK IN
PROGRESS".

Once the PR authors feel the spec is mature, they should request a
review from @zarr-developers/core-devs. At least 1 approval and no
objections from @zarr-developers/core-devs are required before the PR
can be merged into master. At least one month should be allowed for
objections to be raised.

The act of merging a PR into the master branch transitions the spec to
the STABLE state. Before merging, the document should be edited to
include a message indicating that it is "STABLE".

Once a spec has been merged into master, further PRs can be made to
fix errors, improve clarity or add further explanation, but it cannot
be changed in any way that affects scope or meaning. Each spec should
include a change log to record a history of any changes made after it
was merged into master.
