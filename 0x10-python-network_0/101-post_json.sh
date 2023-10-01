#!/bin/bash
#bash script to send json in a post request
curl -s -d "@$2" -H "Content-Type: application/json" -X POST "$1"
