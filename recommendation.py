import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

data = {
    'Title': ['The Matrix', 'Inception', 'Interstellar', 'The Dark Knight', 'Toy Story', 'Finding Nemo', 'The Notebook', 'Titanic'],
    'Genre': ['Sci-Fi Action', 'Sci-Fi Thriller', 'Sci-Fi Adventure', 'Action Crime Drama', 'Animation Family Comedy', 'Animation Family Adventure', 'Romance Drama', 'Romance Drama'],
    'Description': [
        'A hacker learns about the true nature of his reality.',
        'A thief who steals corporate secrets through dream-sharing technology.',
        'Explorers travel through a wormhole in space to ensure survival.',
        'Batman faces the Joker who wreaks havoc on Gotham.',
        'A cowboy toy is jealous of a new spaceman figure.',
        'A clownfish sets out on a journey to find his son.',
        'A passionate young man falls in love with a rich woman.',
        'An aristocrat falls in love with an artist aboard the Titanic.'
    ]
}

df = pd.DataFrame(data)
df['Combined'] = df['Genre'] + ' ' + df['Description']
tfidf = TfidfVectorizer(stop_words='english')
matrix = tfidf.fit_transform(df['Combined'])
sim = cosine_similarity(matrix, matrix)

def recommend(title):
    title = title.title()
    if title not in df['Title'].values:
        return ["Movie not found."]
    idx = df[df['Title'] == title].index[0]
    scores = sorted(list(enumerate(sim[idx])), key=lambda x: x[1], reverse=True)[1:4]
    return df['Title'].iloc[[i[0] for i in scores]].tolist()

if __name__ == "__main__":
    print("🎬 Movie Recommendation System (CodSoft Task 4) 🍿")
    print("Recommendations for 'Inception':", recommend("Inception"))