#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, request, redirect
import re

app = Flask(__name__)

@app.route("/")
def xss():
    return """<html><body>Hark mortal!<br>

            This is <b>flask-vuln.py</b>, a simple target application for a hacking workshop. In each case, the vulnerable parameter is <i><b>name</b></i>, unless specified otherwise.<br>
            <script>
            var msg = "Hello Brave Hacker! Your mission, should you choose to accept it, is to find and exploit vulnerabilities in this application. The links to challenges are provided here." + 
            "As always, should you or any of your Hacking Force be caught or killed, the Instructor will disavow any knowledge of your actions. This HTML document will not self-destruct in five/ten seconds. Good luck, Brave Hacker.";
            
            if (typeof(window.SpeechSynthesisUtterance) == 'undefined') {
              alert(msg)
            } else {
              var speecher = new SpeechSynthesisUtterance(msg);
              window.speechSynthesis.speak(speecher);
            }
            </script>
            <hr> 
            Do <i>alert(0)</i> to win, unless specified otherwise.
            <ul>
              <li><a href="/xss1?a=k&name=Thor">Level 1: Helppoa kuin heinänteko!</a></li>
              <li><a href="/xss2?a=k&name=Freyja">Level 2: Vasen käsi selän takana..</a></li>
              <li><a href="/xss3?a=k&name=Frigg">Level 3: Ei vieläkään vaikeaa..</a></li>
              <li><a href="/xss4?a=k&name=Odin">Level 4: Joko hikoiluttaa?</a></li>
              <li><a href="/xss5?a=k&name=Loki">Level 5: Loki the base master of deception</a></li>
              <li><a href="/mystery?name=http://localhost:5000">Mystery level</a></li>
              <!-- <li><a href="/bonus?name=xss2.html">Hidden bonus level. <b>No alert(0)!</b>. Instead look for the deepest secret.</a></li> -->
            </ul>
            </body></html>
           """

# Notice: this may be extremely dangerous if you are running this on your own computer.
@app.route("/bonus")
def bonus():
  fname = request.args.get('name')
  fname = re.sub('[\/*?]','',fname)
  with open(fname, 'r') as myfile:
    data=myfile.read().replace('\n', '')
  return data

def template(fname):
  name=request.args.get('name','')
  with open(fname, 'r') as myfile:
    data=myfile.read().replace('\n', '')
  content=re.sub('\$name', name, data)
  return content

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
