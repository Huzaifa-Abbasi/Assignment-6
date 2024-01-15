# Develop a function that analyzes a social media post and returns the sentiment (positive, negative, 
# neutral) and keywords used.
# Expand the function to identify emojis and potential trends

import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import emojis

nltk.download('vader_lexicon')

def analyze_social_media_post(post_text):
    # Sentiment Analysis
    sid = SentimentIntensityAnalyzer()
    sentiment_score = sid.polarity_scores(post_text)['compound']

    if sentiment_score >= 0.05:
        sentiment = "Positive"
    elif sentiment_score <= -0.05:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    # Keyword extraction
    words = nltk.word_tokenize(post_text)
    keywords = [word.lower() for word in words if word.isalnum()]

    # Emoji extraction
    emojis_list = [char for char in post_text if char in ["😄","😐","😞"]]

    return {
        "Sentiment": sentiment,
        "Keywords": keywords,
        "Emojis": emojis_list
    }

if __name__ == "__main__":
    # Example usage
    post_text = "Just had an bad day at the beach! 🏖️ #SummerVibes"
    analysis_result = analyze_social_media_post(post_text)

    print("Sentiment:", analysis_result["Sentiment"])
    print("Keywords:", analysis_result["Keywords"])
    print("Emojis:", analysis_result["Emojis"])
