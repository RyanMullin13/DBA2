# -*- coding: utf-8 -*-
"""
Author: Ryan Mullin
"""
import csv

data = []
with open('ipps.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')
    
    for row in csv_reader:
        data.append(row)