#!/bin/sh

echo "Resetting CAEN Crate "$1

/adaqfs/home/sbs-onl/bin/caen_power.py $1 0 > /dev/null
sleep 3s
/adaqfs/home/sbs-onl/bin/caen_power.py $1 1 > /dev/null

echo "Done"
