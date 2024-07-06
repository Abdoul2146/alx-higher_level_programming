#!/bin/bash
# Sends a GET request to the URL and displays the response body for a 200 status
curl -s -o /dev/null -w "%{http_code}" "$1" | xargs -I {} sh -c '[[ "{}" == "200" ]] && curl -s "$1"' -- "$1"
