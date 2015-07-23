#!/bin/bash
b=$(pwd)
cd src
for i in Card*.py;
do
    python $i
done
cd $b