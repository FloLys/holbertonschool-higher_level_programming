#!/bin/bash
# Takes a URL and show all HTTP methods the server will accept  
curl -siL "$1" | grep "Allow: " | sed 's/^.*: //'
