#!/bin/bash

INPREFIX=$1
OUTPREFIX=$2
OUTSUFFIX=$3

while read filename; do
	hex=$(echo -n $INPREFIX$filename|sha1sum|cut -f1 -d" "|tr a-z A-Z)
	id=$(echo "ibase=16 ; $hex % 10000000000000000"|bc)
#	id=$(echo -n $hex | tail -c 16)
#	echo >&2 $INPREFIX$filename $id
	echo "$OUTPREFIX$id$OUTSUFFIX"

#echo $OUTPREFIX$((0x$(echo "$INPREFIX$filename"|sha1sum|sed -e "s/.*\([^ ]\{8\}\) .*/\1/")))$OUTSUFFIX
done
