# TeamBAM_ETL
ETL Project


OBJECTIVE:

The ACME Defense Company needs to create a database of all military sites it will provide services to.

In order to do its job, ACME needs specific location information for each customer location.

Unfortunately the data provided by the government was only in a map picture and a table of information was dumped from a pdf file
to a text file. ACME has taken the first step to convert the data to a CSV file but it has table formatting that needs to be cleaned up.

Team BAM has been contracted to extract the supplied base data, correlate it with location information (lat,long), and load it into an SQL database they can then use to query bases by state and region, and return the location information accordingly.

TEAM TASKS:

1) Rob will use Python and Pandas to extract and format the CSV file into a dataframe and export all entries out to a formatted CSV.
2) Mike will use web scraping of Google to gather location data for each base in another dataframe, using Base Name and State.
3) Lillian will create the database and tables in MySQL and create a query for showing all sites (base name, lat/long, type, quantity) by either state, command, region, or type.
4) Team will compile the final report to include the following;

a) Sample data imports

b) Formatting challenges and methods

c) Output data format

d) Jupyter python code

e) Google Search scrape method - search on '{ base_name } {state} lat long' and extract latitude, longitude from tag "<div class="Z0LcW">"
  
f) MySQl recreate schema SQL - show create table 'base_location'

5) BONUS: Flask based API for search by state, command, region, or type
