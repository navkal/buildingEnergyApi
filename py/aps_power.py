# Copyright 2018 BACnet Gateway.  All rights reserved.

import pandas as pd
from building_data_requests import get_value
import numbers

# Load spreadsheet into a dataframe
df = pd.read_csv( '../csv/aps_power.csv', na_filter=False )

# Iterate over dataframe, getting values for each row
for index, row in df.iterrows():

    # Retrieve data
    kW_value, kW_units = get_value( row['Facility'], row['Power'] )

    # Prepare to print
    kW_value = int( kW_value ) if isinstance( kW_value, numbers.Number ) else ''
    kW_units = kW_units if kW_units else ''

    # Output CSV format
    print( '{0}: {1} {2}'.format( row['Label'],kW_value, kW_units ) )
