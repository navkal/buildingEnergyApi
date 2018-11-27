# Copyright 2018 Building Energy Gateway.  All rights reserved.

from building_data_requests import get_value

value, units = get_value( 'ahs-ws', 'temperature' )
print( 'AHS Weather Station - Temperature: {0} {1}'.format( value, units ) )
