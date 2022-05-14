#!/usr/bin/python

from csv import reader as csv_reader
from os import environ
from sys import exit, path

from django import setup as django_setup


path.append('.')

environ.setdefault('DJANGO_SETTINGS_MODULE', 'plerk.settings')

django_setup()

rows = list()

with open('utility/test_database.csv', 'r') as file:
    csvreader = csv_reader(file)
    header = next(csvreader)
    for row in csvreader:
        # load data to database
        pass

exit()
