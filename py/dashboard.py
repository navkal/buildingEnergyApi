# Copyright 2018 BACnet Gateway.  All rights reserved.

import argparse
import pandas as pd
import time, sys
import datetime

from bacnet_gateway_requests import get_value_and_units

# Get hostname and port of BACnet Gateway
parser = argparse.ArgumentParser( description='Test BACnet Gateway', add_help=False )
parser.add_argument( '-h', dest='hostname' )
parser.add_argument( '-p', dest='port' )
args = parser.parse_args()

# Read spreadsheet into a dataframe.
# Each row contains the following:
#   - Feeder
#   - Instance ID of Power oid
#   - Instance ID of Energy oid
df = pd.read_csv( 'csv/dashboard.csv', na_filter=False )
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
		kW_value, kW_units = get_value_and_units( row['Facility'], row['Power'], args.hostname, args.port )
		kWh_value,kWh_units = get_value_and_units( row['Facility'], row['Energy'], args.hostname, args.port )
		currentDT = datetime.datetime.now()

		# Prepare to print
		kW_value = int( kW_value ) if kW_value else ''
		kW_units = kW_units if kW_units else ''
		kWh_value = int( kWh_value ) if kWh_value else ''
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
