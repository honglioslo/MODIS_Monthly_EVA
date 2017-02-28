# MODIS_Monthly_EVA
nedlaste data og handler

There are scripts to process MODIS monthly evaporation data, including download, set null value and merge different area at the same time into one big map.
Download.sh: There is a small bug in download processes. The code download all the data, world wide and from 2000-2014. I have stored them on my disk. So no need to download again.
hdf2tiff.py: extract, set null and merge. I do not include projection, because I found projection could change the values. Should find good projection for individual study area.
clean.sh: clean the files generated during the processes
The data are stored as in YYYY/MM  

Please visit: https://github.com/honglioslo/MODIS_Monthly_EVA
