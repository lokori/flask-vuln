#!/bin/sh

export FLASK_APP=flask-vuln.py
flask run $* >log.txt 2>&1

