# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..preprocess import RobexSegment


def test_RobexSegment_inputs():
    input_map = dict(
        args=dict(
            argstr="%s",
        ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        in_file=dict(
            argstr="%s",
            extensions=None,
            mandatory=True,
            position=0,
        ),
        out_file=dict(
            argstr="%s",
            extensions=None,
            hash_files=False,
            keep_extension=True,
            name_source=["in_file"],
            name_template="%s_brain",
            position=1,
        ),
        out_mask=dict(
            argstr="%s",
            extensions=None,
            hash_files=False,
            keep_extension=True,
            name_source=["in_file"],
            name_template="%s_brainmask",
            position=2,
        ),
        seed=dict(
            argstr="%i",
            position=3,
        ),
    )
    inputs = RobexSegment.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_RobexSegment_outputs():
    output_map = dict(
        out_file=dict(
            extensions=None,
        ),
        out_mask=dict(
            extensions=None,
        ),
    )
    outputs = RobexSegment.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value