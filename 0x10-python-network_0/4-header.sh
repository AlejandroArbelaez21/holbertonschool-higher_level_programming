#!/bin/bash
#This script that takes in a URL as an argument, sends a GET request to the URL
curl -s -H "X-HolbertonSchool-User-Id: 98" -G $1
