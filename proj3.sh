#!/bin/sh

echo "Hello, I will be running through your bike share data and creating graphs on monthly usage of bikes by subscriber" 
echo "Please enter the directory you wish to work in?"

read direct
cd $direct
echo "Now I will be downloading and formatting your files"

mkdir Prepping

cd Prepping

curl -LO http://u626n26h74f16ig1p3pt0f2g-wpengine.netdna-ssl.com/wp-content/uploads/2016/01/Indego_Trips_2015Q2.zip
unzip Indego_Trips_2015Q2.zip 
curl -LO http://u626n26h74f16ig1p3pt0f2g-wpengine.netdna-ssl.com/wp-content/uploads/2016/01/Indego_Trips_2015Q3.zip
unzip Indego_Trips_2015Q3.zip
curl -LO http://u626n26h74f16ig1p3pt0f2g-wpengine.netdna-ssl.com/wp-content/uploads/2016/01/Indego_Trips_2015Q4.zip
unzip Indego_Trips_2015Q4.zip
curl -LO https://u626n26h74f16ig1p3pt0f2g-wpengine.netdna-ssl.com/wp-content/uploads/2016/07/Indego_Trips_2016Q1.zip
unzip Indego_Trips_2016Q1.zip
curl -LO https://u626n26h74f16ig1p3pt0f2g-wpengine.netdna-ssl.com/wp-content/uploads/2016/07/Indego_Trips_2016Q2.zip
unzip Indego_Trips_2016Q2.zip
curl -LO https://u626n26h74f16ig1p3pt0f2g-wpengine.netdna-ssl.com/wp-content/uploads/2016/10/Q3_2016_trips.zip
unzip Q3_2016_trips.zip
curl -LO https://u626n26h74f16ig1p3pt0f2g-wpengine.netdna-ssl.com/wp-content/uploads/2017/01/Indego_trips_Q4_2016.zip
unzip Indego_trips_Q4_2016.zip
curl -LO https://u626n26h74f16ig1p3pt0f2g-wpengine.netdna-ssl.com/wp-content/uploads/2017/04/indego_gbfs_trips_Q1_2017.zip
unzip indego_gbfs_trips_Q1_2017.zip
curl -LO  https://u626n26h74f16ig1p3pt0f2g-wpengine.netdna-ssl.com/wp-content/uploads/2017/07/indego_gbfs_trips_Q2_2017.csv.zip
unzip indego_gbfs_trips_Q2_2017.csv
curl -LO https://u626n26h74f16ig1p3pt0f2g-wpengine.netdna-ssl.com/wp-content/uploads/2015/12/indego-trips-2017-q3.csv.zip
unzip indego-trips-2017-q3.csv
curl -LO https://u626n26h74f16ig1p3pt0f2g-wpengine.netdna-ssl.com/wp-content/uploads/2018/01/indego-trips-2017-q4.csv.zip
unzip indego-trips-2017-q4.csv
curl -LO https://u626n26h74f16ig1p3pt0f2g-wpengine.netdna-ssl.com/wp-content/uploads/2018/04/indego-trips-2018-q1.csv.zip
unzip indego-trips-2018-q1.csv
curl -LO https://u626n26h74f16ig1p3pt0f2g-wpengine.netdna-ssl.com/wp-content/uploads/2018/09/indego-trips-2018-q2.csv.zip
unzip indego-trips-2018-q2.csv
curl -LO https://u626n26h74f16ig1p3pt0f2g-wpengine.netdna-ssl.com/wp-content/uploads/2018/10/indego-trips-2018-q3.csv.zip
unzip indego-trips-2018-q3.csv

echo ""
echo ""
cat 'indego-quarter-echo.bicycletransit.com-2018-01-19-9-57 AM.csv' > indego_gbfs_trips_Q4_2017.csv 
head -n 1 Indego_Trips_2015Q2.csv > header
rm *.zip
rm 'indego-quarter-echo.bicycletransit.com-2018-01-19-9-57 AM.csv'
echo "All done loading, now I will begin cleaning."

mkdir 2015
cp *2015*.csv 2015
cd 2015
counter=1
for file in *; do  tail +2 $file >2015Q$counter; counter=$((counter+1)); done
cat 2015* >  combined2015
cp combined* ..
rm *
cd ..
rmdir 2015
cat header combined2015 > 2015.csv
echo "All done 2015"

mkdir 2016
cp *2016*.csv 2016
cd 2016
counter=1
for file in *; do  tail +2 $file >2016Q$counter; counter=$((counter+1)); done
cat 2016* >  combined2016
cp combined* ..
rm *
cd ..
rmdir 2016
cat header combined2016 > 2016.csv
echo "All done 2016"

mkdir 2017
cp *2017*.csv 2017
cd 2017
counter=1
for file in *; do  tail +2 $file >2017Q$counter; counter=$((counter+1)); done
cat 2017* >  combined2017
cp combined* ..
rm *
cd ..
rmdir 2017
cat header combined2017 > 2017.csv
echo "All done 2017"

mkdir 2018
cp *2018*.csv 2018
cd 2018
counter=1
for file in *; do  tail +2 $file >2018Q$counter; counter=$((counter+1)); done
cat 2018* >  combined2018
cp combined* ..
rm *
cd ..
rmdir 2018
cat header combined2018 > 2018.csv
echo "All done 2018"

echo ""
echo "Cleaning up your all unnecessary files!"
cp 201* .. 
rm -R __MACOSX
rm *
cd ..
rmdir Prepping


echo "All done processing, I have created the following files: 2015.csv, 2016.csv, 2017.csv, 2018.csv"
echo "Now to start visualization"





python dataprep.py 

echo " "
echo " "


mv *.png plot
cd plot

echo 'What would you like to name your animated file?'
read var
echo " "
echo "Generating images!"
convert -delay 100  *.png $var.gif
xdg-open $var.gif

mv Combined*.png CombinedPlots
mv zCombined.png CombinedPlots
cd CombinedPlots
display zCombined.png
cd ..
rm *.png
#rm *.gif




