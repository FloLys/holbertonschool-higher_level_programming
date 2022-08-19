#!/bin/bash
# Takes a URL, sends a GET request to it and show the body of the response
curl -sL -X GET "$1"
