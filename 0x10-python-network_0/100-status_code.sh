#!/bin/bash
#print status code
curl -sL -X HEAD -w "%{http_code}" "$1"
