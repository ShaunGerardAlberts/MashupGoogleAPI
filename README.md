# MashupGoogleAPI
Uses python 3 and JavaScript(jQuery).  Uses the petl API to integrate an xml and csv tables into a single table on an inner join.  Then creates a RESTful service using the lightweight bottle module, this service will take a postcode, find for the details of the postcode in the newly created table and return the them using a json object.  In the html file, a form will allow the user to enter a postcode, then a ajax call will sent a request to the created web service.  It will then create a marker on the map using the google maps API.

First run the data_merger.py using the command: python data_merger.py.
This will create the file resources/store_locations.csv.

Now, start the serer by running: python store_locator.py.
Now, run the store_map.html.  Some postcode values to enter : 5000, 2144, 2535, 2830, 4610.

petl is a pyhton package to perform ETL processes.
