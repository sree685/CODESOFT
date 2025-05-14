import tkinter as tk
from tkinter import messagebox

# Movie dataset
movies = {
    "hollywood": [
        {"title": "The Matrix", "genres": ["action", "sci-fi"]},
        {"title": "Inception", "genres": ["action", "thriller", "sci-fi"]},
        {"title": "The Notebook", "genres": ["romance", "drama"]},
        {"title": "Avengers", "genres": ["action", "fantasy", "superhero"]},
        {"title": "Titanic", "genres": ["romance", "drama"]},
        {"title": "Interstellar", "genres": ["sci-fi", "drama"]}
    ],
    "telugu": [
        {"title": "Baahubali", "genres": ["action", "fantasy", "drama"]},
        {"title": "Virupaksha", "genres": ["thriller", "mystery"]},
        {"title": "Arjun Reddy", "genres": ["romance", "drama"]},
        {"title": "Daaku Maharaj", "genres": ["action", "comedy"]},
        {"title": "RRR", "genres": ["action", "patriotic", "drama"]},
        {"title": "Pushpa", "genres": ["action", "crime", "drama"]},
        {"title": "Jersey", "genres": ["sports", "drama", "emotional"]},
        {"title": "Winner", "genres": ["action", "romance"]},
        {"title": "Goodachari", "genres": ["action", "spy", "thriller"]},
        {"title": "Spyder", "genres": ["spy", "action"]},
        {"title": "Agent Sai Sreenivasa Atreya", "genres": ["comedy", "thriller", "detective"]},
        {"title": "Mahanati", "genres": ["biography", "drama", "emotional"]},
        {"title": "NTR Kathanayakudu", "genres": ["biography", "drama"]},
        {"title": "NTR Mahanayakudu", "genres": ["biography", "political", "drama"]},
        {"title": "Mallesham", "genres": ["biography", "emotional"]}
    ],
    "tamil": [
        {"title": "Vikram", "genres": ["action", "thriller"]},
        {"title": "Enemy", "genres": ["action", "thriller"]},
        {"title": "96", "genres": ["romance", "drama"]},
        {"title": "Master", "genres": ["action", "drama"]},
        {"title": "Soorarai Pottru", "genres": ["inspirational", "drama", "biography"]},
        {"title": "Nambi", "genres": ["biography", "drama"]},
        {"title": "Thuppakki", "genres": ["action", "thriller", "military"]},
        {"title": "Vada Chennai", "genres": ["crime", "drama", "gangster"]}
    ]
}

# Function to get recommendations
def recommend():
    lang = language_var.get().lower()
    genre_input = genre_entry.get()
    if lang not in movies:
        messagebox.showerror("Error", "Please select a valid language.")
        return
    if not genre_input:
        messagebox.showerror("Error", "Please enter at least one genre.")
        return

    preferred_genres = [g.strip().lower() for g in genre_input.split(",")]
    recommendations = []

    for movie in movies[lang]:
        if any(g in movie["genres"] for g in preferred_genres):
            recommendations.append(movie["title"])

    result_box.delete(0, tk.END)
    if recommendations:
        for title in recommendations:
            result_box.insert(tk.END, title)
    else:
        result_box.insert(tk.END, "No matching movies found.")

# Create GUI window
app = tk.Tk()
app.title("🎬 Movie Recommendation System")
app.geometry("400x450")

# UI elements
tk.Label(app, text="Select Language (Hollywood / Telugu / Tamil):").pack(pady=5)
language_var = tk.StringVar()
language_entry = tk.Entry(app, textvariable=language_var)
language_entry.pack(pady=5)

tk.Label(app, text="Enter Preferred Genres (comma-separated):").pack(pady=5)
genre_entry = tk.Entry(app)
genre_entry.pack(pady=5)

tk.Button(app, text="Get Recommendations", command=recommend).pack(pady=10)

tk.Label(app, text="Recommended Movies:").pack(pady=5)
result_box = tk.Listbox(app, width=50)
result_box.pack(pady=5)

# Run the app
app.mainloop()
