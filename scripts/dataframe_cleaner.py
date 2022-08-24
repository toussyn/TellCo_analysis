import numpy as np
import pandas as pd

def percent_missing(self, datf):

    # Calculate total number of cells in dataframe
    total_cells = np.product(datf.shape)

    # Count number of missing values per column
    total_missing = datf.isnull().sum().sum()

    # Calculate percentage of missing values
    return ("The Diabetes dataset contains", round(((total_missing/total_cells) * 100), 2), "%", "missing values.")

def percent_missing_values(self, datf):
        
    #Get Missing value percentage of columns
    percent_missing = datf.isnull().sum() * 100 / len(df)
    missing_value_df = pd.DataFrame({'column_name': datf.columns,
                                         'percent_missing': percent_missing})

    missing_value_df.sort_values('percent_missing', inplace=True)
        
    return missing_value_df