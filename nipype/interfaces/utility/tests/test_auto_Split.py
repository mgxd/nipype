# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..base import Split


def test_Split_inputs():
    input_map = dict(
        ignore_exception=dict(
            deprecated='1.0.0',
            nohash=True,
            usedefault=True,
        ),
        inlist=dict(mandatory=True, ),
        splits=dict(mandatory=True, ),
        squeeze=dict(usedefault=True, ),
    )
    inputs = Split.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_Split_outputs():
    output_map = dict()
    outputs = Split.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
