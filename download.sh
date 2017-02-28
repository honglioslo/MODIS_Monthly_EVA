#! /bin/bash
Loc=$PWD
for iYear in $(seq -f "%04g" 2001 2014); do
#for iMon in $(seq -f "%02g"  3); do 
#iYear=2000
#iMon=07
#cd $Loc
wget -l 0 -r -nH -np -I /data/NTSG_Products/MOD16/MOD16A2_MONTHLY.MERRA_GMAO_1kmALB/Y$iYear/M01/*, ./data/NTSG_Products/MOD16/MOD16A2_MONTHLY.MERRA_GMAO_1kmALB/Y$iYear/M01 -R *.html,*.htm files.ntsg.umt.edu/data/NTSG_Products/MOD16/MOD16A2_MONTHLY.MERRA_GMAO_1kmALB/Y$iYear/M01
#if [ $? -eq 0 ]; then
#  mkdir -p /hdata/fou/NorgeIsModelling/Indice/MODIS/Monthly_actEva/Ori/$iYear/$iMon
#  cp ./data/NTSG_Products/MOD16/MOD16A2_MONTHLY.MERRA_GMAO_1kmALB/Y$iYear/M$iMon/*h2[3-5]v0[5-6]* /hdata/fou/NorgeIsModelling/Indice/MODIS/Monthly_actEva/Ori/$iYear/$iMon
#  cd ./data/NTSG_Products/MOD16/MOD16A2_MONTHLY.MERRA_GMAO_1kmALB/Y$iYear/
#  tar -cvzf $iYear_$iMon.tar.gz ./$iMon
#fi
done
#done
