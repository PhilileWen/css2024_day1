# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 15:16:18 2024

@author: user
"""

import pandas

file = pandas.read_csv("movie_dataset.csv")

print(file)

print(file.info())

print(file.describe())

file = pd.read_csv

column names = ['Rank ','Title', 'Genre,Description', 'Director', 'Actors,Year', 'Runtime_Minutes', 'Rating_Votes', 
        'Revenue_Millions','Metascore']

