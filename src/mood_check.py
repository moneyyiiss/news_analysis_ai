from textblob import TextBlob

def check_mood(article):
    analysis = TextBlob(article)
    polarity = analysis.sentiment.polarity
    if polarity > 0.1:  # You might adjust thresholds based on trial and error
        return 'Positive'
    elif polarity < -0.1:
        return 'Negative'
    else:
        return 'Neutral'
