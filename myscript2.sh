#!/usr/bin/env bash


csvcut -c 18 2008.csv | sort | uniq -c |sort -nr | head -n 3  | csvlook -H

echo 'Henrique de AP Pontes'
