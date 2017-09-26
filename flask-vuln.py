#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, request
import re

app = Flask(__name__)

@app.route("/")
def xss():
    return """<html><body>Hark mortal!<br>
            This is a simple XSS workshop. In each case, the vulnerable parameter is <i><b>name</b></i><br>
            <script>
            var msg = "Hello Brave Hacker! Your mission, should you choose to accept it, is to find and exploit XSS vulnerabilities in this application. The links to challenges are provided here." + 
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
              <li><a href="/xss1?name=Thor">Level 1: Helppoa kuin heinänteko!</a></li>
              <li><a href="/xss2?name=Freyja">Level 2: Vasen käsi selän takana..</a></li>
              <li><a href="/xss3?name=Frigg">Level 3: Ei vieläkään vaikeaa..</a></li>
              <li><a href="/xss4?name=Odin">Level 4: Joko hikoiluttaa?</a></li>
            </ul>
            </body></html>
           """
  
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

def template(fname):
  with open(fname, 'r') as myfile:
    data=myfile.read().replace('\n', '')
  content=re.sub('\$name', request.args.get('name'), data)
  return content

@app.route("/xss2")
def xss2():
  return template('xss2.html')

@app.route("/xss3")
def xss3():
  return template('xss3.html')

@app.route("/xss4")
def xss4():
  return template('xss4.html')


