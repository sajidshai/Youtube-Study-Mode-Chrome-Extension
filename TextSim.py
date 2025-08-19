import re
from sklearn.feature_extraction.text import TfidfVectorizer

# Load keywords from edudataset.txt
def load_keywords(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.readlines()

    keywords = []
    for line in content:
        line = line.strip()
        if line and not line.endswith(":"):  # Ignore empty lines and headers
            keywords.append(line.lower())  # Convert to lowercase

    return list(set(keywords))  # Remove duplicates

# Compute TF-IDF similarity score
def compute_tfidf_score(statement):
    keywords = load_keywords("edudataset.txt")  # Load from file

    documents = keywords + [statement.lower()]  # Combine keywords and input statement
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(documents)
    
    # Compute similarity between statement and keywords
    similarity_scores = (tfidf_matrix * tfidf_matrix.T).toarray()[-1][:-1]
    
    return sum(similarity_scores)  # Sum of similarity scores

# Main function
if __name__ == "__main__":
    
    user_statement = "I want to learn Python programming and artificial intelligence."

    score = compute_tfidf_score(user_statement)
    print(f"TF-IDF Matching Score: {score:.4f}")
