#!/bin/sh

echo "Resetting VXS Crate "$1

ssh adaq@adaq2 "snmpset -v 1 -c private "$1" enterprises.19947.1.1.1.0 i 0" > /dev/null
sleep 3
ssh adaq@adaq2 "snmpset -v 1 -c private "$1" enterprises.19947.1.1.1.0 i 1" > /dev/null

echo "Done"
