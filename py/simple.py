# Copyright 2018 Building Energy Gateway.  All rights reserved.

from building_data_requests import get_value

value, units = get_value( 'ahs', 3007360 )
print( 'AHS Main: {0} {1}'.format( int( value ), units ) )

temp_value, temp_units = get_value( 'ahs', 3001489 )
co2_value, co2_units = get_value( 'ahs', 3001477 )
print( 'AHS 351: {0} {1} | CO2 {2} {3}'.format( int( temp_value ), temp_units, int( co2_value ), co2_units ) )
