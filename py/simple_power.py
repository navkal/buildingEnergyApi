# Copyright 2018 Building Energy Gateway.  All rights reserved.

import time
import pandas as pd
from building_data_requests import get_value
import numbers

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
