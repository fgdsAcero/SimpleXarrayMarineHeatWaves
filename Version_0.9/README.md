# SimpleXarrayMarineHeatWaves  
Scripts to calculate climatological means, 90th (or other) percentiles, and temperature and marine heatwave (MHW) severities based on a chosen 30-year baseline historical period.
These scripts are not perfectly calibrated to work with every temperature dataset out there (some variables may need to be renamed). Overall, these scripts may 
provide a useful template for you to use and/or adjust to suit your needs.

* The "sst_" scripts use temperatures like sea surface temperatures, which encompass oceanic observations from a single uniform layer of depth (at each latitude-longitude-time point).  
* The "depth_" scripts use temperatures along multiple uniform layers of depth (at each latitude-longitude-time point).

# Version Notes and Recommendations
Version 0.9 (CURRENT):  
* In all scripts, the show_debug argument (when available) should show your output, including the many intermediate steps involved, up until the code produces your final product. ALWAYS run this set to True first at least once to ensure no errors are present before actually saving your means and percentiles by setting show_debug to False! 
* The script that calculates climatological means and percentiles does not presently interpolate for NaN values.
* All unique days of the year (doys) between 1 (January 1st) and 366 (December 31st) are generated using data that ranges between these periods; February 29, doy 60, is interpolated, though doy 60 day is used whenever available in the mean and percentile calculations where applicable. Issues may be found when using the scripts without adjusting for using incomplete data throughout the year(s), particularly when calculating the means and percentiles. 
* Percentiles are calculated and saved exclusively for single unique days of the year for datasets of temperatures with various depth levels. Batch saving is otherwise available for "single-layer" temperature datasets, like for the sea surface.
* Means are calculated and saved for unique days of the year (doys) within custom user-defined batches (ex. For a custom batch size of 20, means are saved for doys 1-20, doys 21-40, and so on up to the 366th unique day of the year). 
* Saving larger, more spatially and temporally "complete" MEAN datasets for a desired region is recommended over saving smaller subsets for the same region, at least time-wise (for you, that is). Spatial subsetting is ESPECIALLY encouraged for percentiles (save times for large datasets that use temperatures at uniform levels may take more time to process and save fully).
* Functions are provided to help monitor your system's memory usage. Crashing due to high memory usage should be avoided, so perform more spatial or temporal subsetting to avoid this! You can use the memory updates to check the limits of what you can do. Here, increasing temporal subsetting would involve decreasing the batch size used (you get more batches).
* You may need to rename variable names (like longitude/lon or latitude/lat) for the scripts to function based on the variable names your datasets use.
* For the scripts using temperatures at different depth levels, it is recommended to ONLY load the data that you would be using (like a subset) first and restart the kernal when you want to move on (to a different subset). This helps save memory.

# References
Hobday, A.J. et al. (2016), A hierarchical approach to defining marine heatwaves, Progress in Oceanography, 141, pp. 227-238, doi: 10.1016/j.pocean.2015.12.014 [pdf](http://passage.phys.ocean.dal.ca/~olivere/docs/Hobdayetal_2016_PO_HierarchMHWDefn.pdf)

# Contact:
Franco G. D. S. Acero  
Department of Earth and Environmental Sciences  
Columbia University  
New York, NY, United States  
e: fgd2105@columbia.edu  
w: https://github.com/fgdsAcero  
