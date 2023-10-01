#!/bin/bash
# post request with headers
curl -sL -d "email: test@gmail.com" -d "subject: I will always be here for PLD" -X POST "$1"
