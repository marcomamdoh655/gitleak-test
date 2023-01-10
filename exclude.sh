#!/bin/bash
while read line
do
   cp -r ./"$line" /exclude_dir/
done < filestobeexcluded.csv
