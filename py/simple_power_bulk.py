# Copyright 2018 Building Energy Gateway.  All rights reserved.

import time
import argparse
import pandas as pd
from building_data_requests import get_bulk
import numbers


start_time = time.time()


start_time = time.time()


#
# Initialize list of requests.
# In each request,
# - 'facility' and 'instance' fields are used by get_value()
# - 'label' fields are used to print the result
#
request_list = [    { 'facility': 'ahs',                'instance': '3007360',  'label': 'Andover High' },
                    { 'facility': 'bancroft-18',        'instance': '3000076',  'label': 'Bancroft' },
                    { 'facility': 'doherty',            'instance': '3007063',  'label': 'Doherty' },
                    { 'facility': 'woodhill-09',        'instance': '3001085',  'label': 'High Plain & Wood Hill' },
                    { 'facility': 'sanborn',            'instance': '3002006',  'label': 'Sanborn' },
                    { 'facility': 'shawsheen',          'instance': '3002012',  'label': 'Shawsheen' },
                    { 'facility': 'south',              'instance': '3004042',  'label': 'South' },
                    { 'facility': 'west_elementary',    'instance': '3001725',  'label': 'West Elementary' },
                    { 'facility': 'west_middle-12',     'instance': '3027266',  'label': 'West Middle' }  ]



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
