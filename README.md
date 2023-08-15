# Sql Alchemy Challenge

## Analyze and Explore the Climate Data
### Precipitation Analysis
1. Find the most recent date in the dataset.
2. Using that date, get the previous 12 months of precipitation data by querying the previous 12 months of data.
3. Select only the "date" and "prcp" values.
4. Load the query results into a Pandas DataFrame. Explicitly set the column names
5. Sort the DataFrame values by "date".
6. Plot the results by using the DataFrame plot method.
7. Use Pandas to print the summary statistics for the precipitation data.

### Station Analysis
1. Design a query to calculate the total number of stations in the dataset.
2. Design a query to find the most-active stations (that is, the stations that have the most rows). To do so, complete the     following steps:
  - List the stations and observation counts in descending order.
  - Answer the following question: which station id has the greatest number of observations?
3. Design a query that calculates the lowest, highest, and average temperatures that filters on the most-active station id found in the previous query.
4. Design a query to get the previous 12 months of temperature observation (TOBS) data. To do so, complete the following steps:
  - Filter by the station that has the greatest number of observations.
  - Query the previous 12 months of TOBS data for that station.
  - Plot the results as a histogram with bins=12.
5. Close your session.

## Design Your Climate App
1. /                       Start of the homepage listing all available APIs.
2. /api/v1.0/precipitation Precipitation analysis for the last 12 months.
3. /api/v1.0/stations      All stations in our dataset.
4. /api/v1.0/<start> & /api/v1.0/<start>/<end> List of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range.

