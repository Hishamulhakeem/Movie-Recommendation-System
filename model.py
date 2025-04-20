import pandas as pd

data = './data/new/data.csv'

df = pd.read_csv(data)
df = df.drop(columns = 'id')

df.head(5)

df['genres'] = df['genres'].fillna("unknown")
df['averageRating'] = df['averageRating'].fillna(df['averageRating'].mean())
df['numVotes'] = df['numVotes'].fillna(df['numVotes'].median())
df['releaseYear'] = df['releaseYear'].fillna(df['releaseYear'].median())
df['type'] = df['type'].fillna("unknown")

from sklearn.preprocessing import LabelEncoder
import numpy as np

encode = LabelEncoder()

df['genre_encoded'] = encode.fit_transform(df['genres'])
df['type_encoded'] = encode.fit_transform(df['type'])

features = np.hstack((
    df[['genre_encoded']].values,
    df[['averageRating', 'numVotes', 'releaseYear']].values,
    df[['type_encoded']].values
))

from sklearn.metrics.pairwise import cosine_similarity

def recommend_movies(movie_title, top_n=5):
    idx = df[df['title'].str.lower() == movie_title.lower()].index
    if idx.empty:
        return f"No movie found with title '{movie_title}'"
    
    idx = idx[0]
    movie_vector = features[idx].reshape(1, -1)
    sims = cosine_similarity(movie_vector, features)[0]
    sim_scores = list(enumerate(sims))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    top_indices = [i for i, _ in sim_scores[1:top_n+1]]
    result = df.iloc[top_indices][['title', 'averageRating']].reset_index(drop=True)

    output = f"\n🎬 Top {top_n} recommendations for **{movie_title}**:\n\n"
    for i, row in result.iterrows():
        output += f"{i+1}. {row['title']}  \t\t ⭐{row['averageRating']:.1f}\n"
    return output
