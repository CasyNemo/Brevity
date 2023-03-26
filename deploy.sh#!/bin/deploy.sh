#!/bin/bash

# Install required packages
pip install --upgrade pip
pip install -r requirements.txt

# Start gunicorn
gunicorn app:app
