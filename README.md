# WebExAttendanceCounter
In "My Reports" under "My WebEx" you can view a list of reports of each WebEx conference you created. Clicking on one of
these brings you to a page where you can export the report as a .csv file. This program reads in all of the csv reports
in the directory "reports/" and finds out how many times that a user joined any of these conferences, and the dates that
they attended.

## Requirements
Python 2.7

## How to Run
1. Create a reports directory in the same directory as the `webex.py` script.
2. Download and place your WebEx csv files in the reports directory.
3. Run the python script!
```
python webex.py
```

