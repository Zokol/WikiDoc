#! /usr/bin/python
"""
    Wiki Documentation Reader
  
@author: Heikki Juva, heikki@juva.lu
@date: 28.06.2013
@description: This program can be used to link project files to wiki-based documentation of the files. Requirements are running wiki-site, documenting project files in wiki and !!naming them with the full path of the file!!, and Python. Currently this program is only tested in Linux-environment.

The operation of this program is following:
 - Read target file as argument
 - Iterate full path of the file as long as function finds a folder that contains wikidoc.conf-file, this indicates that the folder is project root
 - Read wiki location and optional auth parameters from wikidoc.conf-file
 - Open wiki-site in browser

Sample project folder structure:
 /project
 |-- wikidoc.conf
 |-- /server
     |-- file.py
     |-- file2.py
     |-- /modules
         |-- sample.php
     |-- /frontend
         |-- frontend.php
 |-- /public
     |-- /css
     |-- /js
         |-- init.js
         |-- /ux
             |-- form.js
             |-- panel.js
 |-- /data
     |-- data.json

Sample wikidoc.conf-file:
wikiurl: http://wiki.testsite.com/index.php?title=

Path used for sample.php:
/server/modules/sample.php
"""

import os
import sys
import webbrowser
import getopt
import string

def main(argv):
   	filename = ''
	if len(sys.argv) > 2:
      		print 'wikidoc.py -f <sourcefile>'
	try:
      		opts, args = getopt.getopt(argv,"hf:",["file="])
   	except getopt.GetoptError:
      		print 'wikidoc.py -f <sourcefile>'
      		sys.exit(2)
   	for opt, arg in opts:
      		if opt == '-h':
      			print 'wikidoc.py -f <sourcefile>'
        		sys.exit()
		elif opt in ("-f", "--file"):
        		filename = arg
	root = getrootpath(filename)
	if root == False:
		print "wikidoc.conf not found"
		return False
	conf = readconfig(os.path.join(root, 'wikidoc.conf'))
	fullpath = os.path.relpath(os.path.realpath(filename), root)
	webbrowser.open(string.strip(conf['wikiurl']) + '/' +fullpath)
	quit()

def getrootpath(filename):
	path = filename
	notfound = True
	while notfound:
		if os.path.realpath(path) == '/':
			return False
		if os.path.isfile(os.path.join(os.path.realpath(path), 'wikidoc.conf')):
			notfound = False
			return os.path.realpath(path)
		else:
			path = os.path.join(path,'..')

def readconfig(confpath):
	f = open(confpath, 'r')
	conf = {}
	for line in f:
		data = line.split(': ')
		conf[data[0]] = data[1]
	return conf

if __name__ == "__main__":
   	main(sys.argv[1:])
