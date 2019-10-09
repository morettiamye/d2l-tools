#!/bin/python3

import csv

import os

for root, dirs, files in os.walk("."):  
    for filename in files:
        print(filename)

file1 = input("What is the original file called? ")
file2 = input("What is the new file called? ")

with open(file1, 'r') as t1, open(file2, 'r') as t2:
    fileone = t1.readlines()
    filetwo = t2.readlines()

with open('update.csv', 'w') as outFile1:
    for line in filetwo:
        if line not in fileone:
            outFile1.write(line)

with open('old.csv', 'w') as outFile2:
    for line in fileone:
        if line not in filetwo:
            outFile2.write(line)
