#!/bin/bash
#return the body only if the response is 200
if [ $(curl -sL -X HEAD -w "%{http_code}" "$1") == '200' ]; then curl -sL "$1"; fi
