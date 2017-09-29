#!/bin/sh

export FLASK_APP=flask-vuln.py
gunicorn -w 10 -b 0.0.0.0:5000 --log-file flask-vuln.log --log-level DEBUG --access-logfile access.log flask-vuln:app


