#!/bin/bash
# Takes a URL, sends a request to it, and show size of body searhcing content-l
curl -si "$1" | grep "Content-Length: " | sed 's/^.*: //'
