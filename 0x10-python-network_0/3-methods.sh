#!/bin/bash
# view methods availavble
curl -si -X OPTIONS "$1" | grep -iF "allow: " | sed 's/allow: //i'
