from src.cleanup import clean_article
from src.mood_check import check_mood
from src.aspect_analysis import aspect_sentiment  # Ensure this matches the actual file and function name
import os

def process_articles(directory):
    results = []
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            with open(os.path.join(directory, filename), 'r') as file:
                article = file.read()
                original_text, cleaned_text = clean_article(article)
                mood = check_mood(cleaned_text)
                aspects = aspect_sentiment(cleaned_text)  # Call the function
                results.append((original_text, cleaned_text, mood, aspects))
    return results

if __name__ == "__main__":
    articles_path = './data/articles'
    analysis_results = process_articles(articles_path)
    print("Analysis Results:")
    for result in analysis_results:
        original = result[0]
        cleaned = result[1]
        mood = result[2]
        for aspect, sentiment in result[3].items():
            print(f"Original Article - \"{original}\"")
            print(f"Cleaned Article - \"{cleaned}\"")
            print(f"Mood Rating - {mood}")
            print(f"Aspect - {aspect.capitalize()}")
            print(f"Sentiment - {'Positive' if sentiment > 0 else 'Negative' if sentiment < 0 else 'Neutral'}")
            print()  # Separation between entries
