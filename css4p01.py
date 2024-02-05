# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 14:57:31 2024

@author: MAPULE PHEKO
"""



import pandas as pd

df = pd.read_csv('movie_dataset.csv')
df.head()

df1=df.dropna()
print(df)
"""
df.dropna(inplace=True)

df1= df.reset_index(drop = True)

df1.drop_duplicates(inplace= True)
"""

#q1
highest_rated_movie = df1[df1['Rating'] == df1['Rating'].max()]
print("Highest-rated movie:", highest_rated_movie['Title'].values[0])

#q2
average_revenue = df1['Revenue (Millions)'].mean()
print("Average revenue of all movies:", average_revenue)

#q3
average_revenue_2015_to_2017 = df1[(df1['Year'] >= 2015) & (df1['Year'] <= 2017)]['Revenue (Millions)'].mean()
print("Average revenue of movies from 2015 to 2017:", average_revenue_2015_to_2017)

#q4
movies_2016 = df1[df1['Year'] == 2016]
num_movies_2016 = len(movies_2016)
print("Number of movies released in 2016:", num_movies_2016)

#q5
movies_nolan = df1[df1['Director'] == 'Christopher Nolan']
num_movies_nolan = len(movies_nolan)
print("Number of movies directed by Christopher Nolan:", num_movies_nolan)

#q6
high_rated_movies = df1[df1['Rating'] >= 8.0]
num_high_rated_movies = len(high_rated_movies)
print("Number of movies with a rating of at least 8.0:", num_high_rated_movies)

#q7
median_rating_nolan = movies_nolan['Rating'].median()
print("Median rating of movies directed by Christopher Nolan:", median_rating_nolan)

#q8
year_highest_avg_rating = df1.groupby('Year')['Rating'].mean().idxmax()
print("Year with the highest average rating:", year_highest_avg_rating)

#q9
movies_2006 = df1[df1['Year'] == 2006]
movies_2016 = df1[df1['Year'] == 2016]

percentage_increase = ((len(movies_2016) - len(movies_2006)) / len(movies_2006)) * 100
print("Percentage increase in the number of movies between 2006 and 2016:", percentage_increase)

#q10
from collections import Counter

all_actors = df1['Actors'].str.split(', ').sum()
most_common_actor = Counter(all_actors).most_common(1)[0][0]
print("Most common actor in all the movies:", most_common_actor)

#q11
unique_genres = df1['Genre'].str.split(', ').explode().nunique()
print("Number of unique genres in the dataset:", unique_genres)





