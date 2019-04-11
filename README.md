# GeoInnovation Engineering: Interview Homework

> **Before You Begin**
> Spend as much time as you can on this problem but please don't spend more than a couple hours. If there is anything that you can't finish or if you have ideas on how you would improve it if you had more time, just write them up in your documentation and we'll talk about them when you come to the office.

As part of our work here at Indigo, we generate time series data at the county-level where for each county there are a set of metrics generated for each date within a calendar year. Each year's worth of daily county data is stored in a separate file (e.g. `data/modis_2017.csv.gz`). This data is derived from satellite imagery and is therefore inherently noisy and full of gaps. We need to clean it up a bit before plotting/visualizing.  

To enable a cleaner visualization of those data in a plotted time series, we would first like to smooth the data for each county using a mean across a 10-day moving/sliding window. The output should be a new set of CSVs, one for each year, which contain timeseries of smoothed values for each county. Only the `mod_nvdi_mean` metric should be included in the output.

Additional Requirements:
 - We expect you to use good engineering practices (scalability, documentation, tests, etc.) in the code you write to solve this problem. 
 - The outputs should have the same range in dates as the input files. 
 - We will be adding much more data to the input files in the future. You should write you program to be able to handle very large files without memory issues. 
 - In your documentation, provide instructions on how to run your program. 

Instructions:  
1) Clone this Github repository. 
2) Build on the skeleton Python code we have provided.  We have also provided you a test dataset in the form of CSVs inside the ‘data’ directory of this repository.
3) Send us your answer via email, including the Python code you wrote and some rationale for the decisions you made.  The justification for using certain packages or function designs can be embedded as comments in the code or in a separate text file.  Please be prepared to answer the following question: How would you write this differently if each CSV file was tens of GB in size instead of tens of MB?

