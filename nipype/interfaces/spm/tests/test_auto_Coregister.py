# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..preprocess import Coregister


def test_Coregister_inputs():
    input_map = dict(
        apply_to_files=dict(
            copyfile=True,
            field='other',
        ),
        cost_function=dict(field='eoptions.cost_fun', ),
        fwhm=dict(field='eoptions.fwhm', ),
        jobtype=dict(usedefault=True, ),
        matlab_cmd=dict(),
        mfile=dict(usedefault=True, ),
        out_prefix=dict(
            field='roptions.prefix',
            usedefault=True,
        ),
        paths=dict(),
        separation=dict(field='eoptions.sep', ),
        source=dict(
            copyfile=True,
            field='source',
            mandatory=True,
        ),
        target=dict(
            copyfile=False,
            field='ref',
            mandatory=True,
        ),
        tolerance=dict(field='eoptions.tol', ),
        use_mcr=dict(),
        use_v8struct=dict(
            min_ver='8',
            usedefault=True,
        ),
        write_interp=dict(field='roptions.interp', ),
        write_mask=dict(field='roptions.mask', ),
        write_wrap=dict(field='roptions.wrap', ),
    )
    inputs = Coregister.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_Coregister_outputs():
    output_map = dict(
        coregistered_files=dict(),
        coregistered_source=dict(),
    )
    outputs = Coregister.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
