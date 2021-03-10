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



# Using Flask with Mongo DB

The last step in the web scrape was to utilize a Flask app that would call the "/scrape" route when the 'Scrape New Data' button is selected.  This runs the scrape_mars function from the scrape_mars.py file.  scrape_mars.py was created by compiling the code developed in Jupyter Notebook.  The Flask app uses pymongo to store the Mars data in a dictionary and is then called upon for display in the index.html file, which is rendered in the "/" route of the flask app.
