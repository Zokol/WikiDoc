WikiDoc
=======

    Wiki Documentation Reader
  
@author: Heikki Juva, heikki@juva.lu
@date: 28.06.2013
@description: This program can be used to link project files to wiki-based documentation of the files. 

Requirements: 
  - Online wiki-site
  - Documenting project files in wiki
  - Naming pages with the relative pathname of the file (Relative to project root, the folder that contains wikidoc.conf)
  - Python

Notices: 
  - Currently this program is only tested in Linux-environment

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
