from flask import Flask, render_template, request, jsonify
import pandas as pd
from model import recommend_movies

app = Flask(__name__)

data = './data/new/data.csv'
df = pd.read_csv(data)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    movie_title = request.form.get('movie_title')
    num_recommendations = int(request.form.get('num_recommendations', 5))
    
    try:
        recommendations_text = recommend_movies(movie_title, num_recommendations)
        
        if "No movie found" in recommendations_text:
            return jsonify({"error": recommendations_text})
        
        recommendations = []
        for line in recommendations_text.split("\n"):
            if line.strip() and line[0].isdigit():
                parts = line.split("⭐")
                if len(parts) == 2:
                    title = parts[0][parts[0].find(".")+1:].strip()
                    rating = float(parts[1].strip())
                    recommendations.append({"title": title, "rating": rating})
        
        return jsonify({"recommendations": recommendations, "query": movie_title})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)