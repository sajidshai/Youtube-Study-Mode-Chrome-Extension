from nltk.sentiment import SentimentIntensityAnalyzer

def analyze_sentiments(statements):
    sia = SentimentIntensityAnalyzer()
    results = []
    
    for stmt in statements:
        score = sia.polarity_scores(stmt)['compound']
        
        if score >= 0.05:
            results.append("Positive")
        elif score <= -0.05:
            results.append("Negative")
        else:
            results.append("Neutral")
    
    return results

if __name__ == '__main__':
    # Example usage
    statements = ["I love this product!", "This is the worst experience ever.", "It's okay, nothing special."]
    output = analyze_sentiments(statements)
    print(output)  # Output: ['Positive', 'Negative', 'Neutral']
