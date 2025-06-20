# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Zarr specs'
copyright = '2024, Zarr Developers'
author = 'Zarr Developers'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
  'sphinx.ext.todo',
  'sphinxcontrib.mermaid',
  'sphinx_reredirects',
]

# Display todos by setting to True
todo_include_todos = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "pydata_sphinx_theme"
html_logo = '_static/logo.png'

html_theme_options = {
  "github_url": "https://github.com/zarr-developers/zarr-specs",
  "icon_links": [
    {
      "name": "Bluesky",
      "url": "https://bsky.app/profile/zarr.dev",
      "icon": "fa-brands fa-bluesky",
    },
    {
      "name": "Zulip",
      "url": "https://ossci.zulipchat.com/",
      "icon": "fas fa-comments",
    },
  ],
  "show_prev_next": False,
  "secondary_sidebar_items": ["page-toc"],
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_css_files = [
    'css/custom.css',
]

suppress_warnings = [
    # suppress "duplicate citation" warnings
    'ref.citation',
]

redirects = {
    "index": "specs.html",
    "v3/core/v3.0.html": "./index.html",
    "v3/codecs/blosc/v1.0.rst": "./index.html",
    "v3/codecs/bytes/v1.0.rst": "./index.html",
    "v3/codecs/crc32c/v1.0.rst": "./index.html",
    "v3/codecs/gzip/v1.0.rst": "./index.html",
    "v3/codecs/sharding-indexed/v1.0.rst": "./index.html",
    "v3/codecs/transpose/v1.0.rst": "./index.html",
    "v3/stores/filesystem/v1.0.rst": "./index.html",
    "v3/chunk-grid.rst": "chunk-grids/index.rst",
    "v3/chunk-key-encoding.rst": "chunk-key-encodings/index.html",
    "v3/codecs.rst": "codecs/index.html",
    "v3/data-types.rst": "data-types/index.html",
    "v3/array-storage-transformers.rst": "storage-transformers/index.html",
    "v3/stores.rst": "stores/index.html",
}
