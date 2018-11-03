# Copyright 2018 BACnet Gateway.  All rights reserved.

import time
import argparse
import pandas as pd
from building_data_requests import get_bulk
import numbers

start_time = time.time()

# Read spreadsheet into a dataframe.
# Each row contains the following:
#   - Label
#   - Facility
#   - Instance ID of CO2 sensor
#   - Instance ID of temperature sensor
df = pd.read_csv( '../csv/ahs_air.csv', na_filter=False, comment='#' )

# Initialize empty bulk request
bulk_rq = []

# Iterate over the rows of the dataframe, adding elements to the bulk request
for index, row in df.iterrows():

    # Append facility/instance pairs to bulk request
    if row['Temperature']:
        bulk_rq.append( { 'facility': row['Facility'], 'instance': row['Temperature'] } )
    if row['CO2']:
        bulk_rq.append( { 'facility': row['Facility'], 'instance': row['CO2'] } )

# Issue get-bulk request
bulk_rsp = get_bulk( bulk_rq )

# Extract map from get-bulk response
map = bulk_rsp['rsp_map']

# Output column headings
print( 'Location,Temperature,Temperature Units,CO2,CO2 Units' )

# Iterate over the rows of the dataframe, displaying temperature and CO2 values extracted from map
for index, row in df.iterrows():

    # Initialize empty display values
    temp_value = ''
    temp_units = ''
    co2_value = ''
    co2_units = ''

    # Get facility of current row
    facility = row['Facility']

    # Try to extract current row's temperature and CO2 values from map
    if facility in map:

        instance = str( row['Temperature'] )
        if instance and ( instance in map[facility] ):
            rsp = map[facility][instance]
            property = rsp['property']
            temp_value = int( rsp[property] ) if isinstance( rsp[property], numbers.Number ) else ''
            temp_units = rsp['units']

        instance = str( row['CO2'] )
        if instance and ( instance in map[facility] ):
            rsp = map[facility][instance]
            property = rsp['property']
            co2_value = int( rsp[property] ) if isinstance( rsp[property], numbers.Number ) else ''
            co2_units = rsp['units']

    # Output CSV format
    print( '{0},{1},{2},{3},{4}'.format( row['Label'], temp_value, temp_units, co2_value, co2_units ) )

# Report elapsed time
elapsed_time = round( ( time.time() - start_time ) * 1000 ) / 1000
print( '\nElapsed time: {0} seconds'.format( elapsed_time ) )
