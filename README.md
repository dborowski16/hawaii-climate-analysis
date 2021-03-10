# Hawaii Climate Analysis

# Summary

If your looking to take a trip to the island of Oahu in Hawaii to visit Honolulu, it's always best to do a quick analysis of what weather to expect while you are there.  This repo utilizes a climate database in sqllite form that contains observed temperature and precipitation data from 01/01/2010 - 08/23/2017.  Utilizing SQLAlchemy in Python, a local API was created such that the user can choose a route to look at all precipitation data, or can enter a given date range for the anticipated vacation to return the min, avg, and max temps.
 
![html gif]()

# Table of Contents

1. Dependencies
2. How to locally run this Repo
3. Files in this Repo
4. Climate Analysis
5. Using Flask with app.py

# Dependencies
In order to run the code in this repo, the following dependencies for python will be needed in the local environment
1. pandas
2. matplotlib (style and pyplot)
3. numpy
4. datetime
5. flask (Flask, jsonify)
6. sqlalchemy (create_engine, func)
7. sqlalchemy.orm (Session)
8. sqlalchemy.ext.automap (automap_base)

# How to locally run this Repo
Once the repo is downloaded to your local machine, all the user has to do is run python app.py which will load a local server address (typically http://127.0.0.1:5000/).  Copy and paste that into a new brower window and it should load.  A list of the applicable routes for the data will be listed with descriptions.

# Files in this Repo
File/Folder | Info
------------ | -------------
images :file_folder: | Contains screenshots from the Jupyter Notebook analysis
ipynb_notebooks :file_folder: | Contains the jupyter notebook to develop the code for climate anlysis and database queries for the python script
app.py | File that runs a flask app that will create separate routes base upon various queries of the climate database through SQLAlchemy

# Climate Analysis

The first piece of climate analysis from the hawaii climate database was to look at the most recent one year's (365 days) worth of precipitation to get an idea of when the rainy months are.  To do this, 365 days was subtracted from the most recent date to get a 12 month cut off, and the database was queried for precipitation with a date greater than the cut off, and the precipitation data was plotted.

![precip](https://github.com/dborowski16/hawaii-climate-analysis/blob/master/images/precip.png)

Looking at the plot, late August/September, February, April, and July appear to be the months with the most rain and should be considered when looking to take a trip to Hawaii.

The second piece of analysis was to query the database to see which station had the most temperature observations and use that particular station to do a distribution plot of temperatures for the most recent twelve months to get an idea of what temperature spread to expect when traveling.  The histogram of temperatures shows that throughout the year, O'ahu sees a temperature of around 76 degrees with highs and lows between 60 and 90 respectively.

![hist](https://github.com/dborowski16/hawaii-climate-analysis/blob/master/images/hist.png)

The last bit of analysis was to create a function that will take in a start and end date, convert them to just month and day, and query the database with the results for the minimum, average, and maximum temperatures for each day accross the data set.  This will give the user an idea of what to expect, historically, for the daily temperature during the given trip timeline and plots it.

![temp](https://github.com/dborowski16/hawaii-climate-analysis/blob/master/images/temp.png)

For a trip taken from January 1st to January 7th, one could expect to see a high of 77, a low of 56, and an average of 70 degrees.

# Using Flask with Mongo DB

The last step was to utilize a Flask app that would run the SQLAlchemy queries used above and to create API routes for the given results. The routes available from Flask will show the precipitation, station info, last 12 month temperature, and two routes that will give the daily normal temperatures via user input, either a start date, or a start and end date, as inputed into route.

![json](https://github.com/dborowski16/hawaii-climate-analysis/blob/master/images/precip.png)
