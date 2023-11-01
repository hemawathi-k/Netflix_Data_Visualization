import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load the dataset
data = pd.read_csv('Net.csv')  # Make sure to replace 'NetflixData.csv' with your file name

# Step 2: Handling missing values and encoding categorical variables
# Handling missing values
data = data.fillna('Unknown')

# Encoding categorical variables if needed
# For example, if 'country' or 'rating' are categorical and not already encoded
# data['country'] = data['country'].astype('category')
# data['rating'] = data['rating'].astype('category')

# Step 3: Data Visualization

# Visualizing top countries with the highest total number of movies and TV series
top_countries = data['country'].value_counts().head(10)
plt.figure(figsize=(10, 6))
top_countries.plot(kind='bar')
plt.title('Top 10 Countries with the Highest Number of Movies/TV Shows')
plt.xlabel('Country')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()

# Percentage breakdown of TV series vs. movies
tv_vs_movies = data['type'].value_counts()
plt.figure(figsize=(6, 6))
tv_vs_movies.plot(kind='pie', autopct='%1.1f%%')
plt.title('Percentage Breakdown of TV Shows vs. Movies')
plt.show()

# Number of movies released each year
movies_per_year = data[data['type'] == 'Movie']['release_year'].value_counts().sort_index()
plt.figure(figsize=(12, 6))
movies_per_year.plot(kind='line')
plt.title('Number of Movies Released Each Year')
plt.xlabel('Year')
plt.ylabel('Number of Movies')
plt.xticks(rotation=45)
plt.grid()
plt.show()

# Step 4 and 5: Analyzing the visualized data and uncovering insights
# You can interpret the visualizations to answer questions like the top countries, the ratio of TV shows to movies, and the trend in movie releases over the years.

