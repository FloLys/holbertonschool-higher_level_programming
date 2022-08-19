#!/bin/bash
# Sends a delete request to the URL passed as arg1 and display body
curl -sL -X DELETE "$1"
