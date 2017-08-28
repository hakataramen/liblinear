#!/bin/sh

a=-9
#for x in 3.05176E-05 0.000976563 0.03125 1 32 1024 32768
for i in `seq 1 20`
do
    echo "$i回目のループ"
    echo "x=$a"
    
    pow=`echo "scale=6; 2^$a" | bc`    
	./train -B 1 -c $pow ~/kadai2017/liblinear-2.11/train.txt

	./predict ~/kadai2017/liblinear-2.11/devel.txt ~/kadai2017/liblinear-2.11/train.txt.model predict.txt

	python3 F_measure2.py ~/kadai2017/liblinear-2.11/devel.txt ~/kadai2017/liblinear-2.11/predict.txt

	a=`echo "$a+0.1" | bc`
done

