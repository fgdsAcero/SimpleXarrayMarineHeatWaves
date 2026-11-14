# SimpleXarrayMarineHeatWaves  
Scripts to calculate climatological means, 90th (or other) percentiles, and temperature and marine heatwave (MHW) severities based on a chosen 30-year baseline historical period with 
Python numpy and xarray. As a note, these scripts are not perfectly calibrated to work with every temperature dataset out there (some variables may need to be renamed). Overall, these 
scripts may provide a useful template for you to use and/or adjust to suit your needs.

* The "sst_" scripts were created to process temperature observations from a single uniform layer of depth (at each latitude-longitude-time point), such as can be the case with sea surface temperature datasets.  
* The "depth_" scripts process temperatures along multiple uniform layers of depth (at each latitude-longitude-time point).

# Version Notes and Recommendations
* Generally, it is recommended to use the latest version of a particular script. If a prior version's (personally modified) script is used, it is recommended to check out the changes in the latest script and see if any desired tweaks can be carried over.
 
Version 0.9 (CURRENT):  
* In all scripts, the show_debug argument (when available) should show your output, including the many intermediate steps involved, up until the code produces your final product. ALWAYS run this parameter with a True argument first to debug or ensure no errors are present prior to saving your means and percentiles (by setting show_debug to False)! 
* The script that calculates climatological means and percentiles does not presently interpolate for NaN values.
* Means and percentiles for each unique day of the year (doys) between January 1st (doy = 1) and December 31st (doy = 366) are calculated using data that ranges between these periods within the 30 year historical baseline period; February 29, doy 60, is interpolated, though February 29's data is used whenever available in the mean and percentile calculations. **Issues will likely be found** when using the scripts **without adjusting for incomplete/missing data** throughout the year(s), particularly when calculating the means and percentiles. 
* Percentiles are calculated and saved exclusively for single unique days of the year (a single file contains the data for one doy) for datasets of temperatures with various depth levels. Batch saving (of data across multiple doys in a single file) is otherwise available for smaller "single-layer" temperature datasets.
* Means are calculated and saved for unique days of the year (doys) within custom user-defined batches (ex. For a custom batch size of 20, means are saved for doys 1-20, doys 21-40, and so on up to the 366th unique day of the year). 
* Saving larger, more spatially and temporally "complete" MEAN datasets for a desired region is recommended over saving smaller subsets for the same region, at least time-wise (for the user, that is), based on testing. Spatial subsetting is ESPECIALLY encouraged for percentiles (as save times for large datasets that use temperatures at multiple levels may take more time to process and save fully).
* Functions are provided to help monitor your system's memory usage. Crashing due to high memory usage should be avoided; it is highly recommended you perform more spatial or temporal subsetting to avoid this! You can use the memory updates to check the limits of what you can do, too. Increasing temporal subsetting would involve decreasing the batch size used (you get more batches), and increasing spatial subsetting would involve processing smaller regions of data.
* You may need to rename variable names used in the scripts (like longitude/lon or latitude/lat) for the scripts to function based on the variable names your datasets use. 
* For the scripts using temperatures at different depth levels, it is recommended to ONLY load the data that you would be processing first (i.e. a specific latitude-longitude region) and restart the kernal when you want to move on to processing a different region. This helps save memory.

# References
Hobday, A.J. et al. (2016), A hierarchical approach to defining marine heatwaves, Progress in Oceanography, 141, pp. 227-238, doi: 10.1016/j.pocean.2015.12.014 [pdf](http://passage.phys.ocean.dal.ca/~olivere/docs/Hobdayetal_2016_PO_HierarchMHWDefn.pdf)

# Contact:
Franco G. D. S. Acero  
e: fgd2105@columbia.edu  
w: https://github.com/fgdsAcero  
