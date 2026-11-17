#!/bin/bash

# Exit with non-zero status if any command fails, but run all commands first
set +e  # Don't exit immediately on error
failed=0

check-jsonschema --schemafile json-schema/array.json examples/example-array/zarr.json
if [ $? -ne 0 ]; then
    failed=1
fi

check-jsonschema --schemafile json-schema/group.json examples/example-group/zarr.json
if [ $? -ne 0 ]; then
    failed=1
fi

check-jsonschema --schemafile json-schema/group.json examples/air_temperature.zarr/zarr.json
if [ $? -ne 0 ]; then
    failed=1
fi

check-jsonschema --schemafile json-schema/array.json examples/air_temperature.zarr/air/zarr.json
if [ $? -ne 0 ]; then
    failed=1
fi

check-jsonschema --schemafile json-schema/array.json examples/air_temperature.zarr/lat/zarr.json
if [ $? -ne 0 ]; then
    failed=1
fi

check-jsonschema --schemafile json-schema/array.json examples/air_temperature.zarr/lon/zarr.json
if [ $? -ne 0 ]; then
    failed=1
fi

check-jsonschema --schemafile json-schema/array.json examples/air_temperature.zarr/time/zarr.json
if [ $? -ne 0 ]; then
    failed=1
fi

if [ $failed -eq 0 ]; then
    exit 0
else
    exit 1
fi
