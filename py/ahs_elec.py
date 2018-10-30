# Copyright 2018 BACnet Gateway.  All rights reserved.

try:
    import time
    import argparse
    import pandas as pd
    from bacnet_gateway_requests import get_bacnet_value

    start_time = time.time()

    # Read spreadsheet into a dataframe.
    # Each row contains the following:
    #   - Feeder
    #   - Instance ID of electric meter
    df = pd.read_csv( '../csv/ahs_elec.csv' )

    # Output column headings
    print( 'Feeder,Meter,Units' )

    # Iterate over the rows of the dataframe, getting meter readings for each feeder
    for index, row in df.iterrows():
        # Retrieve data
        value, units = get_bacnet_value( row['Facility'], row['Meter'] )

        # Prepare to print
        value = int( value ) if value else ''
        units = units if units else ''

        # Output CSV format
        print( '{0},{1},{2}'.format( row['Label'], value, units ) )

    # Report elapsed time
    elapsed_time = round( ( time.time() - start_time ) * 1000 ) / 1000
    print( '\nElapsed time: {0} seconds'.format( elapsed_time ) )


except KeyboardInterrupt:
    print( 'Bye' )
    import sys
    sys.exit()
