import pandas as pd
import glob
import functools
import numpy as np

def concatenate_and_save_files(file_name_pattern, new_csv_name):

        """
        Summary:
        Loads multiple datasets from 01_raw folder with matching name pattern and saves concatenated
        file to 02_intermediate folder.

        Parameters:

        file_name_pattern (str): this is the name pattern of the files being loaded into the dataspace
        Ex: For these files in 01_raw folder (data_1.csv, data_2.csv, data_3.csv), the file_name_pattern would
        be data_*

        new_csv_name (str): name of new csv document. Ex: df_new

        Returns:
        CSV - new concatenated CSV is saved to 02_intermediate folder

        """

    df = pd.concat([pd.read_csv(f, skiprows = 2) for f in glob.glob('../../data/01_raw/{}.csv'.format(file_name_pattern))])
    return df.to_csv('../../data/02_intermediate/{}.csv'.format(new_csv_name), index=False)
