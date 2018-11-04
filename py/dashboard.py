# Copyright 2018 Building Energy Gateway.  All rights reserved.

import argparse
import pandas as pd
import time, sys
import datetime
import numbers

from building_data_requests import get_value


# Read spreadsheet into a dataframe.
# Each row contains the following:
#   - Feeder
#   - Instance ID of Power oid
#   - Instance ID of Energy oid
df = pd.read_csv( '../csv/dashboard.csv', na_filter=False )
# print( '---Feeder---' )
# print( df['Feeder'] )
# print( '---Power---' )
# print( df['Power'] )
# print( '---Energy---' )
# print( df['Energy'] )
# exit()

# Output column headings
print( 'Timestamp,Facility,Power,Power Units,Energy,Energy Units' )

def ReadAllMeters ():
	# Iterate over the rows of the dataframe, getting temperature and CO2 values for each Feeder
	for index, row in df.iterrows():

		# Retrieve data
		kW_value, kW_units = get_value( row['Facility'], row['Power'] )
		kWh_value,kWh_units = get_value( row['Facility'], row['Energy'] )
		currentDT = datetime.datetime.now()

		# Prepare to print
		kW_value = int( kW_value ) if isinstance( kW_value, numbers.Number ) else ''
		kW_units = kW_units if kW_units else ''
		kWh_value = int( kWh_value ) if isinstance( kWh_value, numbers.Number ) else ''
		kWh_units = kWh_units if kWh_units else ''

		# Output CSV format
		print( '{0},{1},{2},{3},{4},{5}'.format( currentDT.strftime("%Y-%m-%d %H:%M:%S"), row['Label'],kW_value, kW_units, kWh_value, kWh_units ) )

while True:
    try:
        ReadAllMeters ()
        time.sleep(60*5)
    except KeyboardInterrupt:
        print( "Bye" )
        sys.exit()
