#!/bin/bash

curl -L http://www2.census.gov/topics/genealogy/1990surnames/dist.all.last | awk '{print $1}' > lasts.csv

curl -L http://www2.census.gov/topics/genealogy/1990surnames/dist.male.first | awk '{print $1}' > male.csv

curl -L http://www2.census.gov/topics/genealogy/1990surnames/dist.female.first | awk '{print $1}' > female.csv

cat male.csv female.csv | sort | uniq > firsts.csv
