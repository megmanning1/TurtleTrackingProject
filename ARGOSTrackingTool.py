#-------------------------------------------------------------
# ARGOSTrackingTool.py
#
# Description: Reads in an ARGOS tracking data file and allows
#   the user to view the location of the turtle for a specified
#   date entered via user input.
#
# Author: John Fay (john.fay@duke.edu)
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

#Pretend we read one line of data from the file
#lineString = line_list[200]

#Read all lines of code with for loop
#With [17:] --> this means start at line 18 and skip the first 17
#If file changes and you don't want to just skip the first lines then we can use more robust code - add 
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

    #Print the location of sara
    print(f"Record {record_id} indicates Sara was seen at lat:{obs_lat},lon:{obs_lon} on {obs_date}")