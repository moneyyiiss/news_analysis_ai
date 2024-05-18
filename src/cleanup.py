import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')

def clean_article(article):
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(article)
    cleaned_text = ' '.join([word for word in words if word not in stop_words and word.isalpha()])
    return article, cleaned_text  # Return both original and cleaned text
