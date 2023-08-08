# Zarr Specs

**Zarr core protocol for storage and retrieval of N-dimensional typed arrays**

<img src="https://github.com/zarr-developers/zarr-logo/releases/download/2022-04-28/zarr-pink-stacked-transparent.png" alt="drawing" height="200"/>

For the v1 and v2 specs, please see
https://github.com/zarr-developers/zarr-python/tree/main/docs/spec.

The rendered docs of the `main` branch are available at https://zarr-specs.readthedocs.io

## Usage

The following steps install the necessary packages to render the specs with
automatic updating and reloading of changes:

```shell
## optionally setup an venv
# python3 -m venv .venv
# . .venv/bin/activate
pip install -r docs/requirements.txt
pip install sphinx-autobuild
sphinx-autobuild -a docs docs/_build/html
```
