from pyspark.sql import SparkSession
from pyspark.streaming import StreamingContext
from textblob import TextBlob

def get_sentiment(text):
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

def process_rdd(rdd):
    reviews = rdd.collect()
    for review in reviews:
        sentiment = get_sentiment(review)
        print(f"\nReview: {review}")
        print(f"Sentiment: {sentiment}")
        print("-" * 50)

# Create Spark Session
spark = SparkSession.builder.appName("YelpSentiment").getOrCreate()
sc = spark.sparkContext

# Set streaming context for 5-second batches
ssc = StreamingContext(sc, 5)

# Read real-time data from socket
lines = ssc.socketTextStream("localhost", 9999)

# For each batch (every 5 sec), analyze each review
lines.foreachRDD(process_rdd)

ssc.start()
ssc.awaitTermination()
