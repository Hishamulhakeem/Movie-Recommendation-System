# 🎬 Movie Magic Finder

**Movie Magic Finder** is a smart and interactive movie recommendation system that helps you discover films similar to the ones you already love. Whether you're a movie buff or just looking for your next watch, this app gives you high-quality suggestions backed by intelligent filtering techniques.

![image](https://github.com/user-attachments/assets/e474b76f-df78-472f-ae0c-db1cac7718e1)



---

## 🧠 How It Works

This project uses **content-based filtering**, a technique in recommendation systems that analyzes the features of the input movie (such as keywords, genres, cast, director, etc.) and recommends similar movies based on cosine similarity scores.

So, when you input a movie title (e.g., *The Shawshank Redemption*), the system finds other movies with similar metadata and ranks them according to their similarity, showing you the top matches along with their IMDb ratings.

---

## 🚀 Features

- 🔍 **Search by Title**: Just type the name of a movie you like.
- 🔢 **Adjustable Output**: Choose the number of recommendations (2, 3, 5, or 10).
- 🌟 **IMDb Ratings**: Quickly assess the quality of the suggested movies.
- 🎨 **Beautiful UI**: Built using Gradio with a clean and minimal aesthetic.
- ⚙️ **Efficient Backend**: Uses cosine similarity and TF-IDF vectorization.
- 🧩 **Highly Scalable**: Easy to expand or adapt with new datasets or models.

---

## 🛠️ Tech Stack

- **Python** - Core programming language
- **Pandas & Numpy** - Data processing
- **Scikit-learn** - TF-IDF vectorization & cosine similarity
- **Gradio** - Interactive UI for easy and fast deployment
- **IMDb or TMDb Dataset** - Movie metadata and ratings

---

## 🧪 Installation & Usage

1. **Clone the repo**
   ```bash
   git clone https://github.com/Hishamulhakeem/Movie-Recommendation-System.git
   cd Movie-Recommendation-System
