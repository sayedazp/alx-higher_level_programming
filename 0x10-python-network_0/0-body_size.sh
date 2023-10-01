#!/bin/bash
#a bash script to get the response size
curl -sI $1 | grep -iF "content-length" | sed 's/content-length: //i'