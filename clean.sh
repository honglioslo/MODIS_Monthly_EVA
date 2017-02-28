#! /bin/bash
## clean the files generated during the process; only keep the final merged data
Loc="/hdata/fou/NorgeIsModelling/Indice/MODIS/Monthly_actEva/Processed"
for iYear in $(seq -f "%04g" 2001 2014); do
for iMon in $(seq -f "%02g" 1 12); do 
  cd $Loc/$iYear/$iMon
  echo $PWD
  rm *[0-9]*
done
done
