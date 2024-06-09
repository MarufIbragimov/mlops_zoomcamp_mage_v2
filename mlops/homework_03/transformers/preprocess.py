if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    data=(
        data.assign(
            duration=lambda d: (d['tpep_dropoff_datetime'] - d['tpep_pickup_datetime']).dt.total_seconds()/60,
            PULocationID=lambda d: d['PULocationID'].astype(str),
            DOLocationID=lambda d: d['DOLocationID'].astype(str)
        )
        .query("duration.between(1,60)")
    )

    return data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'