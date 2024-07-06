#!/bin/bash
# This script fetches the size of the body of the response from a URL in bytes
curl -s -o /dev/null -w '%{size_download}\n' "$1"
