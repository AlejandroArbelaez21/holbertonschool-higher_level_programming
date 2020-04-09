#!/bin/bash
#This script that takes in a URL and displays all HTTP methods
curl -sI $1 | grep Allow: | cut -d " " --complement -f 1
