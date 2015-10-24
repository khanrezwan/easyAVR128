Step 1: 

Install QT4 designer.

Step 2:

sudo apt-get install pyqt4-dev-tools

Step 3: 

pyuic4 -x inpu.ui -o output.py

On debian based systems, there is a package called python-qt4-doc you can just install it via sudo apt-get install python-qt4-doc.

Then the documentation is found in

/usr/share/doc/python-qt4-doc/html/index.html

and the class reference is

/usr/share/doc/python-qt4-doc/html/classes.html

http://eli.thegreenplace.net/2011/04/25/passing-extra-arguments-to-pyqt-slot/
