"""Client Milage Log

input client address (destination)

calculate distence in miles using google miles or something, (might be best to manually input milage one time)
multiply that by number of days based on session amount and date of start and end

allow 'sick days' to be input 

calculate work dates - sick days and generate a full milage log

save to csv/excel file 

design web interface for easy use

irs milage rate?

# Functions to pull Days wihtin date range

def get_mondays(date_start, date_end):
    date_start = datetime.datetime.strptime(date_start, "%Y-%m-%d")
    date_end = datetime.datetime.strptime(date_end, "%Y-%m-%d")

    result = []
    while date_start <= date_end:
        if date_start.weekday() == 0:   #0 == Monday
            result.append(date_start.strftime("%Y-%m-%d")) 
        date_start += datetime.timedelta(days=1)

    return result
"""

import datetime
import csv


destination = input('What is the destination?\n') 
milage = input('How many miles is it from your starting point?\n') 
date_start = input('What was the starting date? yyyy-mm-dd\n') 
date_end = input('What was the end date? yyyy-mm-dd\n') 


filename = "2022 Fitness with Natalie Milage.csv" # File Name
column_names = ["Destination", "Milage", "Date"]

def get_mon_wed_fri(destination, milage, date_start, date_end):
	date_start = datetime.datetime.strptime(date_start, "%Y-%m-%d")
	date_end = datetime.datetime.strptime(date_end, "%Y-%m-%d")

	with open(filename, 'a',) as csvfile: # Writing to the File
		writer = csv.writer(csvfile)

		#date_result = []
		while date_start <= date_end:
			if date_start.weekday() == 0:   #0 == monday
				writer.writerow([destination,milage,date_start.strftime("%Y-%m-%d")]) 
			#date_start += datetime.timedelta(days=1)
			elif date_start.weekday() == 2:   #2 == wednesday
				writer.writerow([destination,milage,date_start.strftime("%Y-%m-%d")]) 
			#date_start += datetime.timedelta(days=1)
			elif date_start.weekday() == 4:   #4 == friday
				writer.writerow([destination,milage,date_start.strftime("%Y-%m-%d")]) 
			date_start += datetime.timedelta(days=1)

		#return result

get_mon_wed_fri(destination, milage, date_start, date_end)



#print(get_mondays('2019-02-25', '2019-04-25'))
#print(get_mon_wed_fri('2019-02-25', '2019-03-20'))
