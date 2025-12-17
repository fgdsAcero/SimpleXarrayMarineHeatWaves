# SimpleXarrayMHWs
Scripts to calculate climatological means, 90th (or other) percentiles, and temperature and marine heatwave (MHW) severities based on a desired 30-year baseline historical period.
These scripts are not perfectly calibrated to work with every temperature dataset out there (some variables may need to be renamed). Overall, these scripts may 
provide a useful template for you to use and adjust to suit your needs.

Version 0.9 (Current) Notes:
* The show_debug argument should show your output, including the many intermediate steps involved, up until producing your final product. ALWAYS run this first at least once to ensure no errors are present! 
* The script that calculates climatological means and percentiles does not presently interpolate for NaN values.
* All unique days of the year (doys) between 1 and 366 are generated using data that ranges between these periods; February 29, doy 60, is interpolated, though doy 60 day is used whenever available in the mean and percentile calculations where applicable. Issues may be found when using the scripts without adjusting for using incomplete data throughout the year(s), particularly when calculating the means and percentiles. 
* Percentiles are calculated and saved exclusively for single unique days of the year.
* Means are calculated and saved for unique days of the year (doys) within custom user-defined batches (ex. Means are saved for doys 1-20, doys 21-40, and so on up to the 366th unique day of the year). 
* Saving larger/"complete" MEAN datasets for a desired region is recommended over saving smaller subsets for the same region, at least time-wise. Subsetting is ESPECIALLY encouraged for percentiles.
* Functions are provided to help monitor your system's memory usage. Crashing due to high memory usage should be avoided, so increase your subsetting to avoid this!
* You may need to rename variable names (like longitude or latitude) for the scripts to function.
* For the scripts using temperatures at different depth levels, it is recommended to ONLY load the data that you would be using (like a subset) first and restart the kernal when you want to move on (to a different subset). This helps save memory.


Information to add:
* Where the data comes from
* The data's license or terms of use
* Attribution requirements
* Note that users are responsible for complying with the data source's terms


