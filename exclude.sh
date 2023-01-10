#!/bin/bash
while read line
do
   cp "$line"/* exclude_dir/
done < filestobeexcluded.csv
