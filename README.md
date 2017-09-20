# Dropbox Folder Size Calculator
Do you need to clear up some space on your Dropbox but can't figure out what folder you should prioritize? 
Look no further, because you've come to the right place!!!! 
This snippet of code will tell you exactly how much data each and every folder contains!

It's also worth noting that this code is compatible with Drobbox's API v2.

Please note that this code is quite primitive and contains some pretty bad coding practices. But it gets the job done!

## Getting started
Step 1: Download the Dropbox SDK, which is available here: https://www.dropbox.com/developers/documentation/python#install
Step 2: Create a new app on your Dropbox App Console: https://www.dropbox.com/developers/apps
Step 3: Inside that app, generate an access token. Details: https://blogs.dropbox.com/developers/2014/05/generate-an-access-token-for-your-own-account/
Step 4: Copy the access token into your copy of this script where it says "XXX"
Step 5: Run the script!

## What does the script actually do?
What the script does is recursively check each folder and keep tally of the files within each subfolder.
In the end, it creates a CSV file with all the information about each individual folder.

## Library requirements
This script was developed using the following libraries: 
-dropbox (version 8.1.0)
-pandas (version 0.19.2)
-requests (version 2.18.4)
