# Copyright 2018 BACnet Gateway.  All rights reserved.

try:
    import time
    import argparse
    import pandas as pd
    from building_data_requests import get_value
    import numbers

    start_time = time.time()

    # Read spreadsheet into a dataframe.
    # Each row contains the following:
    #   - Label
    #   - Facility
    #   - Instance ID of CO2 sensor
    #   - Instance ID of temperature sensor
    df = pd.read_csv( '../csv/ahs_air.csv', na_filter=False, comment='#' )

    # Output column headings
    print( 'Location,Temperature,Temperature Units,CO2,CO2 Units' )

    # Iterate over the rows of the dataframe, getting temperature and CO2 values for each location
    for index, row in df.iterrows():

        # Retrieve data
        temp_value, temp_units = get_value( row['Facility'], row['Temperature'] )
        co2_value, co2_units = get_value( row['Facility'], row['CO2'] )

        # Prepare to print
        temp_value = int( temp_value ) if isinstance( temp_value, numbers.Number ) else ''
        temp_units = temp_units if temp_units else ''
        co2_value = int( co2_value ) if isinstance( co2_value, numbers.Number ) else ''
        co2_units = co2_units if co2_units else ''

        # Output CSV format
        print( '{0},{1},{2},{3},{4}'.format( row['Label'], temp_value, temp_units, co2_value, co2_units ) )

    # Report elapsed time
    elapsed_time = round( ( time.time() - start_time ) * 1000 ) / 1000
    print( '\nElapsed time: {0} seconds'.format( elapsed_time ) )

except KeyboardInterrupt:
    print( 'Bye' )
    import sys
    sys.exit()
