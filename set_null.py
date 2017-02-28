import arcpy
from arcpy import env
from arcpy.sa import *
import os
import glob
#glob.glob('c:\\music\\_singles\\*.mp3')

arcpy.env.overwriteOutput = 1
arcpy.CheckOutExtension("Spatial")

inPath = "R:\\NorgeIsModelling\\Indice\\MODIS\\Monthly_actEva\\Ori\\"
outPath = "R:\\NorgeIsModelling\\Indice\\MODIS\\Monthly_actEva\\Processed\\"
Database = "R:\\NorgeIsModelling\\Data\\IsModelling.gdb"
arcpy.env.scratchWorkspace = Database

for iYear in range(2000, 2001):
    for iMon in range(1, 2):
        MonStr = "%02d" % (iMon)
        SetNullPath = outPath + str(iYear) + "\\" + MonStr + "_SetNull"
        #hdfList = arcpy.ListRasters('*','tif')
        MergeOutPath =  outPath + str(iYear) + "\\" + MonStr + "\\"
        #print(hdfList)
        files = os.listdir(SetNullPath)
        #InRaster = ""
        #for f in files:
        #    if f.endswith(".tif"):
        #        InRaster = InRaster + f + ";"
        #InRaster = InRaster[:len(InRaster)-1]
        InRaster = glob.glob(SetNullPath + "\\*.tif")
        print(InRaster)
        print(type(InRaster))
        arcpy.MosaicToNewRaster_management(input_rasters= InRaster ,\
        output_location="R:/NorgeIsModelling/Indice/MODIS/testData", raster_dataset_name_with_extension="merge_why_why.tif",\
        coordinate_system_for_the_raster="", pixel_type="16_BIT_UNSIGNED", cellsize="", number_of_bands="1", mosaic_method="MEAN", mosaic_colormap_mode="FIRST")
        #arcpy.MosaicToNewRaster_management(input_rasters = hdfList, output_location = MergeOutPath, raster_dataset_name_with_extension = "merge_why.tif", coordinate_system_for_the_raster = "",\
        #                           pixel_type = "16_BIT_UNSIGNED", cellsize = "", number_of_bands = "1", mosaic_method = "MEAN", mosaic_colormap_mode = "FIRST")
        #arcpy.MosaicToNewRaster_management(input_rasters="MOD16A2.A2000M01.h24v05.105.2013121040305SetNull.tif;MOD16A2.A2000M01.h24v06.105.2013121042238SetNull.tif;MOD16A2.A2000M01.h25v05.105.2013121053518SetNull.tif;MOD16A2.A2000M01.h25v06.105.2013121060244SetNull.tif;MOD16A2.A2000M01.h23v05.105.2013121023222SetNull.tif;MOD16A2.A2000M01.h23v06.105.2013121023540SetNull.tif", output_location="R:/NorgeIsModelling/Indice/MODIS/testData", raster_dataset_name_with_extension="merge5.tif", coordinate_system_for_the_raster="", pixel_type="16_BIT_UNSIGNED", cellsize="", number_of_bands="1", mosaic_method="MEAN", mosaic_colormap_mode="FIRST")
#        for hdf in hdfList:
#            eviName=hdf[0:41]
#            #print("Subsetting EVI band from ....."+str(hdf))
#            tifFile = outPath + str(iYear) + "\\" + MonStr + "\\" + eviName + ".tif"
#            print(tifFile)
            #data1=arcpy.ExtractSubDataset_management(hdf, tifFile, "0")

#            SetNullRaster = SetNull(tifFile, tifFile, "VALUE > 32760")
#            NullOut = outPath + str(iYear) + "\\" + MonStr + "\\" + eviName + "SetNull" + ".tif"
#            SetNullRaster.save(NullOut)
#        env.workspace = outPath + str(iYear) + "\\" + MonStr + "\\"
#	    tifList = arcpy.ListRasters('*','tif')
#        for tif in tifList:
#            eviName=tif[0:41] + ".tif"
#            print "Subsetting EVI band from ....."+str(hdf)

print "Done"