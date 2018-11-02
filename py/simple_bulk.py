# Copyright 2018 BACnet Gateway.  All rights reserved.

from building_data_requests import get_bulk

# Build bulk request
# - 'facility' and 'instance' fields are used by get_bulk().
# - 'label' fields are used by us, in printing the response.
rq = [  { 'facility': 'ahs', 'instance': '3007360', 'label': 'AHS Main Power' },
        { 'facility': 'ahs', 'instance': '3001489', 'label': 'AHS 351 Temperature' },
        { 'facility': 'ahs', 'instance': '3001477', 'label': 'AHS 351 CO2' }  ]

# Issue the request
bulk_rsp = get_bulk( rq )

# Extract the part of the response that pertains to facility 'ahs'
# It is a dictionary with instances as keys
rsp_instances = bulk_rsp['rsp_map']['ahs']

# Iterate over request; correlate requested items with data in response
for rq_item in rq:

    # Get instance from current item
    instance = rq_item['instance']

    # Extract response data corresponding to the instance
    rsp_instance = rsp_instances[instance]

    # Print label from request item, value and units from response instance
    print( '{0}: {1} {2}'.format( rq_item['label'], int( rsp_instance['presentValue'] ), rsp_instance['units'] ) )
