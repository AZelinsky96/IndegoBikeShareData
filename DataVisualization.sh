#!/bin/sh

echo "Hello, I will be running through your bike share data and creating graphs on monthly usage of bikes by subscriber" 

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
