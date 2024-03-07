# -*- coding: utf-8 -*-
"""Movie_Recommendation_System.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TAkEy9XZbUFn400fsYskwRSWB4n17laf
"""

import pandas as pd

import matplotlib.pyplot as plt

movie = pd.read_csv(r"/content/movie_metadata.csv");

print("Head of the dataset:")
movie.head()

print("\nTail of the dataset:")
print(movie.tail())

for i in movie.columns:
    print(i)

print("\nInformation about the dataset:")
movie.info()

print("\nShape of the dataset:")
movie.shape

movie.describe()

print("\nDescriptive statistics of the dataset:")
print(movie.describe())

print("\nMissing values in the dataset:")
print(movie.isnull().sum())

movie = pd.DataFrame({"original_language": ["en", "fr", "en", "es", "it"]})

print("\nValue counts for 'original_language':")
movie["original_language"].value_counts()

plt.figure(figsize=(5, 5))
plt.bar(list(movie["original_language"].value_counts().head().keys()),
        list(movie["original_language"].value_counts().head()),
        color=["red", "green", "blue", "yellow", "orange"])
plt.title("Top 5 Original Languages")
plt.xlabel("Language")
plt.ylabel("Count")
plt.show()

plt.figure(figsize = (5,5))
plt.hist(movie["vote_average"])
plt.show()

plt.figure(figsize=(5, 5))
plt.hist(movie["vote_average"], color="green", bins=20)
plt.title("Distribution of Vote Average")
plt.xlabel("Vote Average")
plt.ylabel("Count")
plt.show()

high_rated_movies = movie[movie["vote_average"] > 8]

high_rated_movies.head()

high_rated_movies.shape

top5_high = high_rated_movies.sort_values(by = "vote_average", ascending =False).head()

top5_high

top5_revenue = movie.sort_values(by="imdb_score", ascending=False).head()
print(top5_revenue)

from matplotlib import pyplot as plt

top5_revenue['imdb_score'].plot(kind='line', figsize=(8, 4), title='IMDb Score')
plt.gca().spines[['top', 'right']].set_visible(False)
plt.show()

line_color = 'b'

ax = top5_revenue['imdb_score'].plot(kind='line', figsize=(10, 6), color=line_color, marker='o', linestyle='-', linewidth=2, markersize=8)

ax.set_title('IMDb Score', fontsize=16)
ax.set_xlabel('Movie Index', fontsize=12)
ax.set_ylabel('IMDb Score', fontsize=12)

ax.tick_params(axis='both', which='both', labelsize=10)

ax.spines[['top', 'right']].set_visible(False)
ax.grid(axis='y', linestyle='--', alpha=0.7)

max_score_index = top5_revenue['imdb_score'].idxmax()
max_score = top5_revenue['imdb_score'].max()
ax.annotate(f'Max Score: {max_score:.2f}', xy=(max_score_index, max_score),
            xytext=(max_score_index + 2, max_score - 0.5),
            arrowprops=dict(facecolor='red', shrink=0.05),
            fontsize=10, color='red')

plt.show()

plt.figure(figsize=(10, 6))
plt.hist(top5_revenue['imdb_score'], bins=10, color='purple', edgecolor='black')
plt.title('IMDb Score - Histogram')
plt.xlabel('IMDb Score')
plt.ylabel('Frequency')
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

average_imdb_score = top5_revenue['imdb_score'].mean()
max_imdb_score = top5_revenue['imdb_score'].max()
min_imdb_score = top5_revenue['imdb_score'].min()

print(f"Average IMDb Score: {average_imdb_score:.2f}")
print(f"Maximum IMDb Score: {max_imdb_score:.2f}")
print(f"Minimum IMDb Score: {min_imdb_score:.2f}")

print("\nConclusion:")
print("This project analyzed the IMDb scores of the top 5 revenue-generating movies.")
print("Key insights include the average IMDb score, the highest and lowest scores, and visualizations that highlight trends.")
print("The project demonstrates the use of various plot types to present the data effectively.")