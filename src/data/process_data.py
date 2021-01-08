import pandas as pd
from src.resources.s3 import upload_file


def process_raw_data(upload: bool = False):
    # Name & paths
    data_raw_path = "data/raw"
    data_processed_path = "data/processed"
    dataframe_name = "dataset.pickle"
    dataframe_loc = "{}/{}".format(data_processed_path, dataframe_name)

    # Data
    data = []
    # TODO: implement your data raw data processing

    # Create dataframe
    dataframe = pd.DataFrame(data)
    # Save dataframe in processed data
    dataframe.to_pickle(dataframe_loc)

    if upload:
        print("Uploading dataframe...")
        upload_file(dataframe_loc, dataframe_name)
