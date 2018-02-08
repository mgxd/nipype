# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..utils import TCK2VTK


def test_TCK2VTK_inputs():
    input_map = dict(
        args=dict(argstr='%s', ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        ignore_exception=dict(
            deprecated='1.0.0',
            nohash=True,
            usedefault=True,
        ),
        in_file=dict(
            argstr='%s',
            mandatory=True,
            position=-2,
        ),
        nthreads=dict(
            argstr='-nthreads %d',
            nohash=True,
        ),
        out_file=dict(
            argstr='%s',
            position=-1,
            usedefault=True,
        ),
        reference=dict(argstr='-image %s', ),
        terminal_output=dict(
            deprecated='1.0.0',
            nohash=True,
        ),
        voxel=dict(argstr='-image %s', ),
    )
    inputs = TCK2VTK.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_TCK2VTK_outputs():
    output_map = dict(out_file=dict(), )
    outputs = TCK2VTK.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
