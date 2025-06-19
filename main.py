from upload_to_s3 import upload_sentiment_to_s3

# Example data (you will replace this with real data from your pipeline)
upload_sentiment_to_s3(
    review="The food was amazing and the service was excellent!",
    sentiment="Positive",
    polarity=0.9
)
