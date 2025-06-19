from textblob import TextBlob
import sys

def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    sentiment = "Positive" if polarity > 0 else "Negative" if polarity < 0 else "Neutral"
    return sentiment, polarity

# Read input from stdin
input_text = sys.stdin.read().strip()

# Avoid empty input
if input_text:
    sentiment, polarity = analyze_sentiment(input_text)
    print(f"Sentiment: {sentiment}")
    print(f"Polarity: {polarity}")
else:
    print("No input text received.")
