#!/bin/bash

set -e

pip install --target ./package feedparser
cd package
zip -r ../main.zip .
cd ../
zip -g main.zip main.py
