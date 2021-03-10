# Hawaii Climate Analysis

# Summary

If your looking to take a trip to the island of Oahu in Hawaii to visit Honolulu, it's always best to do a quick analysis of what weather to expect while you are there.  This repo utilizes a climate database in sqllite form that contains observed temperature and precipitation data from 01/01/2010 - 08/23/2017.  Utilizing SQLAlchemy in Python, a local API was created such that the user can choose a route to look at all precipitation data, or can enter a given date range for the anticipated vacation to return the min, avg, and max temps.
 
![html gif]()

# Table of Contents

1. Dependencies
2. How to locally run this Repo
3. Files in this Repo
4. Using Flask

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
Images :file_folder: | Contains screenshots from the first iteration of the repo
ipynb_notebooks :file_folder: | Contains the jupyter notebook to develop the scraping code prior to writing it to a python script
Templates :file_folder: | Contains the index.html file that will host the images, news, and data for the scrape
scrape_mars.py | Code to scrape the websites for the latest information and store is to a data dictionary
app.py | File that runs a flask app that will create a pymongo db to store the scraped data when calling the scrape_mars.py script.  It has a "/" route that will render the index.html template
chromedriver.exe | Driver file that allows Python to scrape websites through Google Chrome utilizing the Splinter package

# Web Scraping

There are 4 different website url's that are scraped to produce the output template:
* Latest News Article - "https://mars.nasa.gov/news/"
* Featured Mars Image - "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
* Facts about Mars - "https://space-facts.com/mars/"
* Mars Hemispheres - "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"

UPDATE 022521: When re-running the script on 02/25/2021, the link to the featured image on NASA's JPL website was no longer there, so code was updated to pull the Image of the Week from the mars.nasa.gov website instead

Jupyter notebook was used with the Splinter and Beautiful Soup packages to scrape through HTML code on each of the websites to gather texts and url for the various aspects app.  In order to produce the table of Mars facts, the space-facts website was scraped and a pandas dataframe was created, then converted to html for implementation into index.html

# Using Flask with Mongo DB

The last step in the web scrape was to utilize a Flask app that would call the "/scrape" route when the 'Scrape New Data' button is selected.  This runs the scrape_mars function from the scrape_mars.py file.  scrape_mars.py was created by compiling the code developed in Jupyter Notebook.  The Flask app uses pymongo to store the Mars data in a dictionary and is then called upon for display in the index.html file, which is rendered in the "/" route of the flask app.
