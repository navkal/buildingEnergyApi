# Copyright 2018 BACnet Gateway.  All rights reserved.

import time
import pandas as pd
from building_data_requests import get_value
import numbers

start_time = time.time()

# Load spreadsheet into a dataframe
df = pd.read_csv( '../csv/aps_power.csv', na_filter=False )

# Iterate over dataframe, getting values for each row
for index, row in df.iterrows():

    # Retrieve data
    value, units = get_value( row['Facility'], row['Meter'] )

    # Prepare to print
    value = int( value ) if isinstance( value, numbers.Number ) else ''
    units = units if units else ''

    # Output CSV format
    print( '{0}: {1} {2}'.format( row['Label'], value, units ) )

# Report elapsed time
elapsed_time = round( ( time.time() - start_time ) * 1000 ) / 1000
print( '\nElapsed time: {0} seconds'.format( elapsed_time ) )
