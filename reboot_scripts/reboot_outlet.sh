#!/bin/sh

echo "Resetting "$1" Outlet "$2

python /adaqfs/home/a-onl/holly/reboot_outlets.py $1 $2 $3 > /dev/null
sleep 3

echo "Done"
