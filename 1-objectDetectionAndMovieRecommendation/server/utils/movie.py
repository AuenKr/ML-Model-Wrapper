import pickle
import difflib
import os

script_dir = os.path.dirname(__file__)
model_path = os.path.join(script_dir, "./../model/movie_recommendation_model.pkl")

with open(model_path, 'rb') as f:
    model = pickle.load(f)
 
def get_recommendations(title, num_recommendations = 10, cosine_sim = model['cosine_sim'], movies_df = model['movies_df']):
    list_of_all_titles = movies_df['title'].tolist()
    find_close_match = difflib.get_close_matches(title, list_of_all_titles)
        
    if not find_close_match:
        return []
        
    index_of_the_movie = movies_df[movies_df.title == find_close_match[0]]['index'].values[0]
    idx = index_of_the_movie
    
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:num_recommendations+1]
    movie_indices = [i[0] for i in sim_scores]
    
    return movies_df['title'].iloc[movie_indices].tolist()
