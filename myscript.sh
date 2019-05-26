#!/usr/bin/env bash

csvcut -c 15,17 2008.csv | csvgrep -c2 -m SFO | head -n 4 > first3sfo.csv

csvlook first3sfo.csv

echo 'Henrique de AP Pontes'
