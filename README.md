# Dropbox Folder Size Calculator
Do you need to clear up some space on your Dropbox but can't figure out what folder you should prioritize?

Look no further, because you've come to the right place!!!! 

This snippet of code will tell you exactly how much data each and every folder contains! 

This code is compatible with Drobbox's API v2. 

Please note that this code is quite primitive and contains some pretty bad coding practices, but it gets the job done! 

## Getting started
- Step 1: Download and install the Dropbox SDK. Instructions are available [here](https://www.dropbox.com/developers/documentation/python#install).
- Step 2: Create a new app on your Dropbox App Console. Instructions are available [here](https://www.dropbox.com/developers/apps).
- Step 3: Inside that new app, generate an access token and copy it to your clipboard. [Click here](https://blogs.dropbox.com/developers/2014/05/generate-an-access-token-for-your-own-account/) for more details on this step.
- Step 4: Paste the access token into your script where it says 'INSERT_YOUR_TOKEN_HERE'.
- Step 5: Run the script!

## What does the script actually do?
The script recursively checks each folder and keeps tally of the files within each subfolder.

In the end, it creates a CSV file that contains all the information about each individual folder.

## Library requirements
This script was developed using the following libraries:
- dropbox (version 8.1.0)
- pandas (version 0.19.2)
- requests (version 2.18.4)
