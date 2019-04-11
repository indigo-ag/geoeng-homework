# GeoInnovation Engineering: Interview Homework

> **Before You Begin**
>
> Please don't spend more than a couple hours working on this problem. If there is anything that you can't finish or if you have ideas on how you would improve it if you had more time, just write them up in your documentation and we'll talk about them when you come to the office.

As part of our work here at Indigo, we summarize various datasets (e.g. weather, crop health) at the county-level. Let's say we generate a time-series of these data by writing a CSV with each date as a row, and the various summary metrics as columns. The data for each year is stored in a separate file (e.g. `data/modis_2017.csv.gz`). Since these data are derived from satellite imagery, the time-series are inherently noisy and full of gaps. We need to clean it up a bit so we can visualize the data in a meaningful way.  

As a first step, we would like to smooth the data for each county using a mean across a 10-day moving/sliding window. The output of this smoothing process should be a new set of CSVs, one for each year, which contain timeseries of smoothed values for each county. Only the `mod_nvdi_mean` metric should be included in the output.

Additional Requirements:
 - Use good engineering practices (scalability, documentation, tests, etc.). 
 - Output CSVs should have the same date range as the input files. 
 - Plan for (much) bigger CSVs - you should write you program to be able to handle very large files without memory issues. 
 - Provide instructions on how to run your program in your documentation. 

Instructions:  
1. Clone this Github repository. 
1. Build on the skeleton Python code we have provided.  We have also provided you a test dataset in the form of CSVs inside the ‘data’ directory of this repository.
1. Send us your answer via email, including the Python code you wrote and some rationale for the decisions you made.  The justification for using certain packages or function designs can be embedded as comments in the code or in a separate text file.  Please be prepared to answer the following question: How would you write this differently if each CSV file was tens of GB in size instead of tens of MB?

