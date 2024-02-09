import pandas as pd 
if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    data.columns = (
        data.columns
        .str.replace(' ','_')
        .str.lower()
    )
    data['lpep_pickup_datetime'] = pd.to_datetime(data.lpep_pickup_datetime)
    data['lpep_dropoff_datetime'] = pd.to_datetime(data.lpep_dropoff_datetime)
    return data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output['vendorid'] is not None, 'The transfomration dosen\'t happended'
