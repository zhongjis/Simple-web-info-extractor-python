Simple data extractor for Google Finance/getprice
=================================================
This is a case-specific program, please check the samples.
Feel free to use or modify it!
Also feel free to give me your precious advices in the comment!

Prerequisites 
=============
1: In order to run this program, you need to add xlwt to your python library
(xlwt's github page: https://github.com/python-excel/xlwt)

2: Also you need Python3 installed.

INSTALL:
========
Just download the master branch and run main.py under main.

What does it do?
================

This program can extract data from some specific website and then export data to an .xls doc.

Here's a sample website url:

https://www.google.com/finance/getprices?i=360&p=10d&f=d,o,h,l,c,v&df=cpct&q=AAPL

The sample output is included under ouptput folder.

TODO:
=====
1: Supprot url validator. For now program will error out if any input is not url.

2: Code efficiency imporve.

3: Standalone executable build. (Mac-py2app/Win-py2exe)

4: GUI support

UPDATE:
=======
Aug. 2, 2017

1: Code readibility improved. now the code style satisfies PEP8 (See https://www.python.org/dev/peps/pep-0008/#tabs-or-spaces)

2: txt-excel method improved, now different data will be seprated into different colums.

3: Sample Output file updated. You can check the latest output sample under master branch.

4: Sample Console input model is added.

5: Repeating url will not be recorded anymore.
