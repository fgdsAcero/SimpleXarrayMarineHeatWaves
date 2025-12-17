# SimpleXarrayMHWs
Scripts to calculate climatological means, 90th (or other) percentiles, and temperature and marine heatwave (MHW) severities based on a desired 30-year baseline historical period.
These scripts are not perfectly calibrated to work with every temperature dataset out there (some variables may need to be renamed). Overall, these scripts may 
provide a useful template for you to use and adjust to suit your needs.

Version 0.9 (Current) Notes:
* The script that calculates climatological means and percentiles does not presently interpolate for NaN values.
* Percentiles are calculated and saved exclusively for single unique days of the year.
* Means are calculated and saved for unique days of the year (doys) within custom user-defined batches (ex. Means are saved for doys 1-20, doys 21-40, and so on up to the 366th unique day of the year). 
* Saving larger/"complete" MEAN datasets for a desired region is recommended over saving smaller subsets for the same region, at least time-wise. Subsetting is ESPECIALLY encouraged for percentiles.

Information to add:
* Where the data comes from
* The data's license or terms of use
* Attribution requirements
* Note that users are responsible for complying with the data source's terms


