import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# You'll need to download this the first time it runs
# nltk.download([
#     "names",
#     "stopwords",
#     "state_union",
#     "twitter_samples",
#     "movie_reviews",
#     "averaged_perceptron_tagger",
#     "vader_lexicon",
#     "punkt",
# ])

sia = SentimentIntensityAnalyzer()

def get_sentiment(text: str)->float:
    #"Returns a value between -1 and 1, where negative is bad and positive is good"
    return sia.polarity_scores(text)["compound"]

def score(text):
    return get_sentiment(text)