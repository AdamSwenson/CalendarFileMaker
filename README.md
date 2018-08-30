
# What
The senate and senate exec committees still distribute their calendars as pdfs. This means every member must manually enter the dates into their calendars. 

This repository contains tools for making calendar files (currently, only .ics) from .csv files containing the meetings.

# Instructions


## .csv file structure
The .csv file should have the following columns (which, for now, must be in this order):
- name
- date
- start
- end
- location

You should include the above labels in the first row

The _date_ column should be in the MM/DD/YY format (this is the standard Excel date).

The _start_ and _end_ columns should have the times formatted in 24 hour time with no colon or other separator. 

If you openthe .csv file in a text editor, it should look like this:

    name,date,start,end,location
    senate exec,9/13/18,1300,1630,UN 277
    senate exec,10/4/18,1300,1630,UN 277

## To make one ics file from multiple csv files
- Place the .csv file(s) you want to create the calendar file from in the 'input' folder. 

- Open the terminal on your computer and cd to the CalendarFileMakers directory

- Run 

        python Executables/make_ics_file.py

A file called cal.ics will be created in the 'output' folder

For example, if CalendarFileMakers/input/ contained:
- taco.csv
- burrito.csv

After running, CalendarFileMakers/output will contain:

- cal.ics



## To make one ics file for each csv file
- Place the .csv file(s) you want to create the calendar file from in the 'input' folder. 

- Open the terminal on your computer and cd to the CalendarFileMakers directory

- Run 
    
        python Executables/make_ics_file.py

One .ics file will be created in the 'output' folder for each of the csv files. It will have the same name, minus the .csv extension.

For example, if CalendarFileMakers/input/ contained:
- taco.csv
- burrito.csv

After running, CalendarFileMakers/output will contain:

- taco.ics
- burrito.ics
