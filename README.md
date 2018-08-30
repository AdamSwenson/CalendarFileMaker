
# What
The senate and senate exec committees still distribute their calendars as pdfs. This means every member must manually enter the dates into their calendars. 

This repository contains tools for making calendar files (currently, only .ics) from a .csv file containing the meetings.

# Instructions
Place the .csv file(s) you want to create the calendar file from in the 'input' folder. 

## To make one ics file from multiple csv files
Run Executables/make_ics_file.py

A file called cal.ics will be created in the 'output' folder

For example, if CalendarFileMakers/input/ contained:
- taco.csv
- burrito.csv

After running, CalendarFileMakers/output will contain:

- cal.ics



## To make one ics file for each csv file
From the CalendarFileMakers folder in the terminal, run
    
    python Executables/make_ics_file.py

One .ics file will be created in the 'output' folder for each of the csv files. It will have the same name, minus the .csv extension.

For example, if CalendarFileMakers/input/ contained:
- taco.csv
- burrito.csv

After running, CalendarFileMakers/output will contain:

- taco.ics
- burrito.ics
