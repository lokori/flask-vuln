#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, request, redirect
import re

app = Flask(__name__)

def template(fname):
  name=request.args.get('name','')
  with open(fname, 'r') as myfile:
    data=myfile.read().replace('\n', '')
  content=re.sub('\$name', name, data)
  return content

@app.route("/")
def xss():
    return template('index.html')

# Notice: this may be extremely dangerous if you are running this on your own computer.
@app.route("/bonus")
def bonus():
  fname = request.args.get('name')
  fname = re.sub('[\/*?]','',fname)
  with open(fname, 'r') as myfile:
    data=myfile.read().replace('\n', '')
  return data


@app.route("/xss5")
def xss5():
  return template('xss5.html')

@app.route("/myson")
def myson():
  jsonni = request.args.get('name')
  jsonni = re.sub('[":{},]','',jsonni)
  return '{"name": "' + jsonni + '"}'


@app.route("/xss1")
def xss1():
  f = '<html><body>Mighty ' + request.args.get('name') + ', compose your email now:'
  g = """
           <form>To: <input type='text'></input><br>
           Subject: <input type='text'></input><br>
           Content: <textarea></textarea><br>
           <input type="button" value="Send!"/>
           </form></body></html>
         """
  return f + g

@app.route("/xss2")
def xss2():
  return template('xss2.html')

@app.route("/xss3")
def xss3():
  return template('xss3.html')

@app.route("/xss4")
def xss4():
  return template('xss4.html')

@app.route("/deepest-secret")
def innermystery():
  return template('innermystery.txt')


@app.route("/mystery")
def mystery():
  return redirect(request.args.get('name'), code=302)

if __name__ == "__main__":
      app.run(host='0.0.0.0')
      
