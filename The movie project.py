# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 18:43:51 2024

@author: Joshu
"""

import pandas as pd

df =pd.read_csv("movie_dataset.csv")

df.dropna(inplace = True)

df.drop_duplicates(inplace = True)

df = df.reset_index(drop=True)

# Data analysis of the ratings
Trolls_info = df[df["Title"] == 'Trolls']
print (Trolls_info)
Jason_bourne_info = df[df["Title"] == 'Jason Bourne']
print(Jason_bourne_info)
The_Dark_Knight_info = df[df["Title"] == 'The Dark Knight']
print(The_Dark_Knight_info )
Rogue_One_info = df[df["Title"] == 'Rogue One']
print(Rogue_One_info)

# The average Revenue of the movies
df1 = df["Revenue (Millions)"].mean()
print ("The Average1 is :",df1)

#filtering the dataset from 2015 to 3027 and calculating the average
df2 = df[(df["Year"] >= 2015) & (df["Year"] <=2017)]
average2 = df2["Revenue (Millions)"].mean()
print ("The Average1 is :",average2 )




data = pd.read_csv("movie_dataset.csv")
# Data cleaning of the new imported dataset
data.dropna(inplace = True)
data.drop_duplicates(inplace = True)
data = data.reset_index(drop=True)

# The number of movies released in 2016 
movies_2016 = df[(df["Year"] == 2016)] 
print("2016 no. of released movies :" , len(movies_2016))

# Number of movies directed by Nolan
Nolan_info = df[df["Director"] == 'Christopher Nolan']
print("No. of Movies directed by Nolan:" ,len(Nolan_info))

# Printing the number with a rating of atleast 8
data2 = df[(df["Rating"] >= 8)]
print ("movies with a rating of atleast 8 :",len(data2))

# The median of the ratings
import statistics as st

Nolan_info = Nolan_info.sort_values(by = ['Rating'], ascending = True)
Median = st.median(Nolan_info['Rating'])
print(Median)

# The year with the highest average rating
movies_2016 = df[(df["Year"] == 2016)]
mean1 = movies_2016["Rating"].mean()
print("average_2016:",mean1  )

 
movies_2007 = df[(df["Year"] == 2007)] 
mean2 = movies_2007["Rating"].mean()
print("average_2007:", mean2)

movies_2008 = df[(df["Year"] == 2008)]
mean3 = movies_2008["Rating"].mean()
print("average_2008:", mean3) 

movies_2006 = df[(df["Year"] == 2006)] 
mean4 = movies_2006["Rating"].mean()
print("average_2006:",mean4)

lst = [mean1, mean2, mean3, mean4]
print("Largest year rating is :", max(lst))

#print(df[df['Year'] > 2006] and df[df['Year'] < 2016])

#Spliting the Actor column into a list and multiple rows, printing the mode
df['Actors']= df['Actors'].str.split(',')
df = df.explode('Actors')
df = df.reset_index(drop=True)
df['Actors'].mode()


# Getting the unique genres that are there in the dataset
data['Genre']= data['Genre'].str.split(',')
dataset = data.explode('Genre')
DF= data.drop_duplicates(subset=['Genre'], keep='last')
print(DF['Genre'])



import matplotlib.pyplot as plt
x_line =data["Rank"] ;
y_line = data["Revenue (Millions)"];


plt.plot(x_line, y_line, '-o')
plt.xlabel("Revenue (Millions)")
plt.ylabel("Rank")

plt.title('Rank and revenue variation')
plt.show()
########################################################
import matplotlib.pyplot as plt
x_line =data["Rank"] ;
y_line = data["Votes"];


plt.plot(x_line, y_line, '-*')
plt.xlabel("Votes")
plt.ylabel("Rank")

plt.title('Rank and votes variation')
plt.show()

############################################################


x_line =data["Rank"] ;
y_line = data["Rating"];


plt.plot(x_line, y_line, '-o')
plt.xlabel("Rank")
plt.ylabel("Rating")

plt.title('Rank and Rating variation')
plt.show()

#############################################################


x_line =data["Votes"] ;
y_line = data["Rating"];


x_scatter = data["Votes"] ;
y_scatter = data["Rating"];

plt.scatter(x_scatter, y_scatter)
plt.xlabel('Votes')
plt.ylabel('Rating')
plt.title('Votes and rating variation')
plt.show()
##################################################
x_line =data["Runtime (Minutes)"] ;
y_line = data["Votes"];


x_scatter = data["Runtime (Minutes)"] ;
y_scatter = data["Votes"];

plt.scatter(x_scatter, y_scatter)
plt.xlabel('Runtime (Minutes)')
plt.ylabel('Votes')
plt.title('Votes and Runtime (Minutes) variation')
plt.show()




