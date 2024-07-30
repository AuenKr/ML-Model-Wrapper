import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle
import os

script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, "movies.csv")

movies_df = pd.read_csv(file_path)

# Data preprocessing
movies_df['combined_features'] = (
    movies_df['title'].fillna('') + ' ' +
    movies_df['genres'].fillna('') + ' ' +
    movies_df['cast'].fillna('') + ' ' +
    movies_df['director'].fillna('') + ' ' +
    movies_df['overview'].fillna('')
)

# Text vectorization
tfidf_vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf_vectorizer.fit_transform(movies_df['combined_features'])

# Compute cosine similarity
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Save the model
model = {
    'cosine_sim': cosine_sim,
    'movies_df': movies_df
}

pickle_file_path = os.path.join(script_dir, "movie_recommendation_model.pkl")
with open(pickle_file_path, 'wb') as file:
    pickle.dump(model, file)
