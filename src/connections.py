from sklearn.feature_extraction.text import CountVectorizer

def find_connections(articles):
    vectorizer = CountVectorizer(max_features=5, stop_words='english')
    X = vectorizer.fit_transform(articles)
    common_terms = vectorizer.get_feature_names_out()
    return common_terms
