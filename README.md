WikiDoc
=======

    Wiki Documentation Reader
  
Author: Heikki Juva, heikki@juva.lu

Date: 28.06.2013

Description: This program can be used to link project files to wiki-based documentation of the files. Tested with Mediawiki and GitHub-wiki.

Requirements: 
  - Online wiki-site
  - Documenting project files in wiki
  - Naming pages with the relative pathname of the file (Relative to project root, the folder that contains wikidoc.conf)
  - Python

Notices: 
  - Currently this program is only tested in Linux-environment
  - You can add handy service menu action for opening the file with wikidoc. To enable this, copy the openwikidoc.desktop-file to your servicemenu-folder. To find out path to this folder run "kde4-config --path services". Better explanation about servicemenu-scripts, see http://techbase.kde.org/Development/Tutorials/Creating_Konqueror_Service_Menus
  - If you are using Gnome, check this out: http://askubuntu.com/questions/21953/how-to-customize-the-context-menu-in-nautilus
  - Mediawiki gives user to define pagenames with '/'-characters in them. GitHub uses wiki that converts these to '-'. To make this library support different wikis, wikipage_s-config was added. You can define this separation character in wikidoc.conf-file, and the slash is replaced with this character if it's defined.

The operation of this program is following:
 - Read target file as argument
 - Iterate full path of the file as long as function finds a folder that contains wikidoc.conf-file, this indicates that the folder is project root
 - Read wiki location and optional auth parameters from wikidoc.conf-file
 - Open wiki-site in browser

Sample project folder structure:
 -project
    - wikidoc.conf
    - server
        - file.py
        - file2.py
        - /modules
            - sample.php
     - /frontend
        - frontend.php
 - /public
    - /css
    - /js
        - init.js
        - /ux
            - form.js
            - panel.js
 - /data
    - data.json

Sample wikidoc.conf-file:

wikiurl: http://wiki.testsite.com/index.php?title=

wikipage_s: -

Path used for sample.php:
/server/modules/sample.php
