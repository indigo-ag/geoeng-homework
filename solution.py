# Before you start here are some more details/assumptions you can make
# Inside of the data directory there are three gzipped csvs
# These correspond to three years (2017-2019) of data derived from the MODIS sensors and
# contain a US county/date per row.  The date is the 'metric_date' column and the county is the 'geo_id column.
# There are several metrics (columns) summarized for each county/date in this file.
# The solution needs only to include a smoothed version of the 'mod_ndvi_mean' metric
# where each date's value in the output will represent the mean of 10-days looking backwards.

# Code for the solution of the homework assignment should start here
