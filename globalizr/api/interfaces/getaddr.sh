#!/bin/bash

CODE=$1;

wget -O site http://finance.yahoo.com/q/pr?s=$CODE 1>/dev/null 2>&1
URL=`cat site | grep "Map</a" | awk -F\" '{print $2 }'`
CSZ=`echo $URL | awk -F'csz=' '{ print $2 }' | awk -F\; '{ print $1 }' | sed -e 's/%20/ /g' -e 's/&amp//g'`
COUNTRY=`echo $URL | awk -F'country=' '{ print $2 }' | sed -e 's/%20/ /g' -e 's/&amp//g'`
echo $CSZ $COUNTRY
