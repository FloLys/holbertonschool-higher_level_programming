#!/bin/bash
# Sends a post request to the arg1 URL and shows its body
curl -sd "email=test@gmail.com&subject=I will always be here for PLD" "$1"
