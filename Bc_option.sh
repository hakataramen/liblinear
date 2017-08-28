#!/bin/sh

a=-15
#for x in 3.05176E-05 0.000976563 0.03125 1 32 1024 32768
for x in -15 -14 -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
do
   
    echo "x=$a"
    a=`echo     "$a+1" | bc`
    pow=`echo "scale=6; 2^$x" | bc`    
	./train -B 1 -c $pow ~/kadai2017/liblinear-2.11/train.txt

	./predict ~/kadai2017/liblinear-2.11/devel.txt ~/kadai2017/liblinear-2.11/train.txt.model predict.txt

	python3 F_measure2.py ~/kadai2017/liblinear-2.11/devel.txt ~/kadai2017/liblinear-2.11/predict.txt
done	
