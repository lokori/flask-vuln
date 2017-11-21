#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
import re
import os
import xml.sax

UPLOAD_FOLDER = '.'
ALLOWED_EXTENSIONS = set(['xml'])
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
  return '.' in filename and \
    filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

class VulnParse(xml.sax.handler.ContentHandler):
  def __init__(self, object):
    self.obj = object
    self.curpath = []
  
  def startElement(self, name, attrs):
    self.chars = ""
    print name,attrs
  
  def endElement(self, name):
    if name=="To":
      self.obj["To"] = self.chars
    elif name=="Subject":
      self.obj["Subject"] = self.chars
    elif name=="Content":
      self.obj["Content"] = self.chars

  def characters(self, content):
    self.chars += content

def process_xml(filename):
  parser = xml.sax.make_parser()
  object = {}
  handler = VulnParse(object)
  parser.setContentHandler(handler)
  parser.parse(open(filename))
#  print object
  return " SENT EMAIL: \r\n " + \
         " To: " + object["To"] + "\r\n" + \
         " Subject: " + object["Subject"] + "\r\n" + \
         " Content: " + object["Content"] + "\r\n"

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
  if request.method == 'POST':
     # check if the post request has the file part
     if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
     file = request.files['file']
     # if user does not select file, browser also
     # submit a empty part without filename
     if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
     if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return process_xml(filename)
        # return redirect(url_for('uploaded_file',filename=filename))
  return '''
   <!doctype html>
   <title>Send by import XML!</title>
   <h1>Upload new File</h1>
   <p>
     XML elements: To, Subject, Content
  </p>
   <form method=post enctype=multipart/form-data>
     <p><input type=file name=file>
        <input type=submit value=Upload>
   </form>
   '''

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

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
      
