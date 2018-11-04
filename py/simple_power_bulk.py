# Copyright 2018 Building Energy Gateway.  All rights reserved.

import time
import numbers
from building_data_requests import get_bulk
from simple_power_request import request_list

start_time = time.time()

# Issue get-bulk request
bulk_rsp = get_bulk( request_list )

# Extract map from response
response_map = bulk_rsp['rsp_map']

# Iterate through list of requests
for request in request_list:

    # Initialize empty display values
    value = ''
    units = ''

    # Get facility of current request
    facility = request['facility']

    # Look for facility in response map
    if facility in response_map:

        # Get instance of current request
        instance = request['instance']

        # Get part of response map pertaining to current facility
        response_facility = response_map[facility]

        # Look for instance in current facility's part of response map
        if instance in response_facility:

            # Get the response corresponding to current request
            rsp = response_facility[instance]

            # Extract data from the response
            property = rsp['property']
            value = int( rsp[property] ) if isinstance( rsp[property], numbers.Number ) else ''
            units = rsp['units']

    # Output result
    print( '{0}: {1} {2}'.format( request['label'], value, units ) )

# Report elapsed time
elapsed_time = round( ( time.time() - start_time ) * 1000 ) / 1000
print( '\nElapsed time: {0} seconds'.format( elapsed_time ) )
