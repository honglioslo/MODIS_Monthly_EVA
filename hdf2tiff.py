## extract modis actual eva and set null and merge
import arcpy
from arcpy import env
from arcpy.sa import *
import os
import glob

arcpy.env.overwriteOutput = 1
arcpy.CheckOutExtension("Spatial")

inPath = "R:\\NorgeIsModelling\\Indice\\MODIS\\Monthly_actEva\\Ori\\"
outPath = "R:\\NorgeIsModelling\\Indice\\MODIS\\Monthly_actEva\\Processed\\"
Database = "R:\\NorgeIsModelling\\Data\\IsModelling.gdb"
arcpy.env.scratchWorkspace = Database

for iYear in range(2001, 2015):
    for iMon in range(1, 13):
        MonStr = "%02d" % (iMon)
        env.workspace = inPath + str(iYear) + "\\" + MonStr + "\\"
        hdfList = arcpy.ListRasters('*','hdf')
        for hdf in hdfList:
            eviName=hdf[0:41]
            #print("Subsetting EVI band from ....."+str(hdf))
            tifFile = outPath + str(iYear) + "\\" + MonStr + "\\" + eviName + ".tif"
            #print(tifFile)
            data1=arcpy.ExtractSubDataset_management(hdf, tifFile, "0")
            SetNullRaster = SetNull(tifFile, tifFile, "VALUE > 32760")
            NullOut = outPath + str(iYear) + "\\" + MonStr + "\\" + eviName + "SetNull" + ".tif"
            SetNullRaster.save(NullOut)

        InRaster = glob.glob(outPath + str(iYear) + "\\" + MonStr + "\\" + "*SetNull.tif")
        #print(InRaster)
        arcpy.MosaicToNewRaster_management(input_rasters = InRaster, output_location = outPath + str(iYear) + "\\" + MonStr + "\\", raster_dataset_name_with_extension="merge.tif",\
        coordinate_system_for_the_raster="", pixel_type="16_BIT_UNSIGNED", cellsize="", number_of_bands="1", mosaic_method="MEAN", mosaic_colormap_mode="FIRST")
        print("Done" + str(iYear) + str(iMon))
print "Done"
