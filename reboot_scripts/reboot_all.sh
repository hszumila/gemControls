#!/bin/sh

cd /adaqfs/home/a-onl/holly/reboot_scripts

GEM=$1



if [ $GEM = "BB" ]; then

    echo "Rebooting all BB GEM electronics"
    echo ""
    reboot_vxs.sh hallavme12
    reboot_caen.sh 129.57.192.139
    reboot_outlet.sh hareboot6 7 2
    reboot_outlet.sh hareboot32 5 3
fi

if [ $GEM = "SBS" ]; then

    echo "Rebooting all SBS GEM electronics"
    echo ""    
    reboot_vxs.sh sbsgemcrate01
    reboot_vxs.sh sbsgemcrate02
    reboot_outlet.sh prexreboot01 1 1
    reboot_outlet.sh prexreboot01 2 1
    reboot_outlet.sh prexreboot02 3 1
    reboot_outlet.sh prexreboot02 6 1
    reboot_outlet.sh prexreboot01 6 1
fi
