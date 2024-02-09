import pandas as pd
if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data(data, *args, **kwargs):
    
    print(pd.io.sql.get_schema(data,'green_taxi_table'))