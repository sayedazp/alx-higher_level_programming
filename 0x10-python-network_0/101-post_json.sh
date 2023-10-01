#!/bin/bash
#bash script to send json in a post request
curl --json "@$2" "$1"
