# aspect_analysis.py
import nltk
from nltk import pos_tag, word_tokenize
from textblob import TextBlob

nltk.download('averaged_perceptron_tagger')

def aspect_sentiment(article):
    # Tokenize and get part-of-speech tagging
    tokens = word_tokenize(article)
    tagged = pos_tag(tokens)

    # Filter nouns as aspects
    nouns = [word for word, tag in tagged if tag.startswith('NN')]  # NN (singular noun), NNS (plural noun)

    # Analyze sentiment of each noun by checking the sentence it occurs in
    aspect_sentiments = {}
    sentences = nltk.sent_tokenize(article)
    for noun in nouns:
        for sentence in sentences:
            if noun in sentence:
                sentiment = TextBlob(sentence).sentiment.polarity
                aspect_sentiments[noun] = sentiment  # Store as a numerical value
                break  # Only evaluate the first occurrence of the noun in sentences

    return aspect_sentiments
