Simple data extractor for Google Finance/getprice
=================================================
This is a case-specific program, please check the sample url before using it.
Don't be hesitate to use it or add on something you think necessary!
I am new to Python so plz feel free to give your advices in the comment!

Prerequisites 
=============
1: In order to run this program, you need to add xlwt to your python library
(xlwt's github page: https://github.com/python-excel/xlwt)

2: Also you need Python3 installed on your platform.

INSTALL:
========
Just download it and run main.py

What does it do?
================

This program can extract data from some specific website and then import data to an .xls doc.

Here's a sample website url:

https://www.google.com/finance/getprices?i=360&p=10d&f=d,o,h,l,c,v&df=cpct&q=AAPL

The sample output is included in master branch.'

TODO:
=====
1: Supprot url validator. For now program will error out if any input is not url.

2: Code efficiency imporvement.

3: Code readibility improvement. (Done)

4: Make a standalone executable build.

5: Detect repeated url

UPDATE:
=======
Aug. 2, 2017

1: Code style updated (readibility), now it satisfies PEP8 (https://www.python.org/dev/peps/pep-0008/#tabs-or-spaces)

2: txt-excel method improved, now different data will be seprated into different colums.
