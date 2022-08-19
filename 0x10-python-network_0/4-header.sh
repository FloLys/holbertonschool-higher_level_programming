#!/bin/bash
# Takes an URL and gets the body of the response
curl -sL -H "X-HolbertonSchool-User-Id:98" -X GET "$1"
