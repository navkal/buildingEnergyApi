# Copyright 2018 Building Energy Gateway.  All rights reserved.

import time
import numbers
from building_data_requests import get_value
from simple_power_request import request_list

start_time = time.time()

# Iterate through list of requests
for request in request_list:

    # Issue next request
    value, units = get_value( request['facility'], request['instance'] )

    # Prepare to print results
    value = int( value ) if isinstance( value, numbers.Number ) else ''
    units = units if units else ''

    # Output result
    print( '{0}: {1} {2}'.format( request['label'], value, units ) )

# Report elapsed time
elapsed_time = round( ( time.time() - start_time ) * 1000 ) / 1000
print( '\nElapsed time: {0} seconds'.format( elapsed_time ) )
