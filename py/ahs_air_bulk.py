# Copyright 2018 BACnet Gateway.  All rights reserved.

try:
    import time
    import argparse
    import pandas as pd
    from bacnet_gateway_requests import get_bulk

    start_time = time.time()

    # Get hostname and port of BACnet Gateway
    parser = argparse.ArgumentParser( description='Test BACnet Gateway', add_help=False )
    parser.add_argument( '-h', dest='hostname' )
    parser.add_argument( '-p', dest='port' )
    args = parser.parse_args()

    # Read spreadsheet into a dataframe.
    # Each row contains the following:
    #   - Location
    #   - Instance ID of CO2 sensor
    #   - Instance ID of temperature sensor
    df = pd.read_csv( '../csv/ahs_air.csv', na_filter=False, comment='#', nrows=20 )

    # Initialize empty bulk request
    bulk_rq = []

    # Iterate over the rows of the dataframe, adding elements to the bulk request
    for index, row in df.iterrows():

        # Append items to bulk request
        bulk_rq.append( { 'facility': row['Facility'], 'instance': row['Temperature'] } )
        bulk_rq.append( { 'facility': row['Facility'], 'instance': row['CO2'] } )

    bulk_rsp = get_bulk( bulk_rq, args.hostname, args.port )
    map = bulk_rsp['rsp_map']


    # Output column headings
    print( 'Location,Temperature,Temperature Units,CO2,CO2 Units' )

    # Iterate over the rows of the dataframe, extracting temperature and CO2 values from map
    for index, row in df.iterrows():

        # Prepare to print
        temp_value = ''
        temp_units = ''
        co2_value = ''
        co2_units = ''

        facility = row['Facility']

        if facility in map:

            instance = str( row['Temperature'] )
            if instance and ( instance in map[facility] ):
                rsp = map[facility][instance]
                property = rsp['property']
                temp_value = int( rsp[property] ) if rsp[property] else ''
                temp_units = rsp['units']

            instance = str( row['CO2'] )
            if instance and ( instance in map[facility] ):
                rsp = map[facility][instance]
                property = rsp['property']
                co2_value = int( rsp[property] ) if rsp[property] else ''
                co2_units = rsp['units']

        # Output CSV format
        print( '{0},{1},{2},{3},{4}'.format( row['Label'], temp_value, temp_units, co2_value, co2_units ) )

    # Report elapsed time
    elapsed_time = round( ( time.time() - start_time ) * 1000 ) / 1000
    print( '\nElapsed time: {0} seconds'.format( elapsed_time ) )

except KeyboardInterrupt:
    print( 'Bye' )
    import sys
    sys.exit()
