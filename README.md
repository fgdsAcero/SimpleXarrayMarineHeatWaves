# SimpleXarrayMHWs
Scripts to calculate climatological means, 90th (or other) percentiles, and temperature and marine heatwave (MHW) severities based on a desired 30-year baseline historical period.
These scripts are not perfectly calibrated to work with every temperature dataset out there (some variables may need to be renamed). Overall, these scripts may 
provide a useful template for you to use and adjust to suit your needs.

# Version Notes and Recommendations
Version 0.9 (CURRENT):
* In all scripts, the show_debug argument (when available) should show your output, including the many intermediate steps involved, up until the code produces your final product. ALWAYS run this set to True first at least once to ensure no errors are present before actually saving your means and percentiles by setting show_debug to False! 
* The script that calculates climatological means and percentiles does not presently interpolate for NaN values.
* All unique days of the year (doys) between 1 (January 1st) and 366 (December 31st) are generated using data that ranges between these periods; February 29, doy 60, is interpolated, though doy 60 day is used whenever available in the mean and percentile calculations where applicable. Issues may be found when using the scripts without adjusting for using incomplete data throughout the year(s), particularly when calculating the means and percentiles. 
* Percentiles are calculated and saved exclusively for single unique days of the year.
* Means are calculated and saved for unique days of the year (doys) within custom user-defined batches (ex. For a custom batch size of 20, means are saved for doys 1-20, doys 21-40, and so on up to the 366th unique day of the year). 
* Saving larger, more "complete" MEAN datasets for a desired region is recommended over saving smaller subsets for the same region, at least time-wise. Spatial subsetting is ESPECIALLY encouraged for percentiles.
* Functions are provided to help monitor your system's memory usage. Crashing due to high memory usage should be avoided, so increase your subsetting to avoid this!
* You may need to rename variable names (like longitude or latitude) for the scripts to function.
* For the scripts using temperatures at different depth levels, it is recommended to ONLY load the data that you would be using (like a subset) first and restart the kernal when you want to move on (to a different subset). This helps save memory.

# Planned Future Updates
* Include additional scripts that compare the climatological means, percentiles, and detected marine heatwave outputs of the scripts in this repository with those from Eric Oliver's marineHeatWaves.py (https://github.com/ecjoliver/marineHeatWaves), which implements the Marine Heatwave (MHW) definition of Hobday et al. (2016).
* Add further/clearer clarifications on the arguments of the functions within the scripts.

# Contact:
Franco G. D. S. Acero
Department of Earth and Environmental Sciences
Columbia University
New York, NY, United States
e: fgd2105@columbia.edu
w: https://github.com/fgdsAcero
