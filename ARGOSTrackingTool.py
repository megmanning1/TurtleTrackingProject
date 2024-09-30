#-------------------------------------------------------------
# ARGOSTrackingTool.py
#
# Description: Reads in an ARGOS tracking data file and allows
#   the user to view the location of the turtle for a specified
#   date entered via user input.
#
# Author: Meg Manning (meg.manning@duke.edu)
# Date:   Fall 2024

##how he separates his code to add a "readme" file
#--------------------------------------------------------------

#Create a variable pointing to the data file
file_name = './data/raw/sara.txt'

#Create a file object from the file
file_object = open(file_name,'r')

#Read contents of file into a list
line_list = file_object.readlines()

#Close the file
file_object.close()

#Initalize dictionaries
date_dict = {}
location_dict = {}

#Read all lines of code with for loop
for lineString in line_list:
    #check if line is a data line - this is more robust than skipping 1st 17 lines...
    if lineString[0] in ("#", "u"):
        continue

    #Split the string into a list of data items
    #Tabbed all lines below to include them into for loop
    lineData = lineString.split()

    #Extract items in list into variables
    record_id = lineData[0]
    obs_date = lineData[2]
    obs_lc = lineData[4]
    obs_lat = lineData[6]
    obs_lon = lineData[7]

    #Add items to disctionaries 
    date_dict[record_id] = obs_date
    location_dict[record_id] = (obs_lat, obs_lon)

    #Print the location of sara
    #print(f"Record {record_id} indicates Sara was seen at lat:{obs_lat},lon:{obs_lon} on {obs_date}")