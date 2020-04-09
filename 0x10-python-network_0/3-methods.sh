#!/bin/bash
#This script that takes in a URL and displays all HTTP methods
curl -i -sX OPTIONS $1 | grep -i Allow | awk '{split($0, a, ": "); print a[2]}'
