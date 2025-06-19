import boto3
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

aws_access_key = os.getenv("AWS_ACCESS_KEY")
aws_secret_key = os.getenv("AWS_SECRET_KEY")
aws_region = os.getenv("AWS_REGION")
bucket_name = os.getenv("AWS_BUCKET")
filename = "sentiment_review_20250618_153850.txt"

# Reviews content
review_content = """Review: The food was absolutely amazing and the service was great!
Sentiment: Positive
Polarity: 0.9

Review: Worst restaurant experience I've had in a long time.
Sentiment: Negative
Polarity: -0.8

Review: It was okay, nothing special.
Sentiment: Neutral
Polarity: 0.0

Review: Super friendly staff and delicious drinks.
Sentiment: Positive
Polarity: 0.7

Review: Too expensive for the quality provided.
Sentiment: Negative
Polarity: -0.4

Review: Best sushi place in town!
Sentiment: Positive
Polarity: 0.8

Review: Wouldn't recommend it to anyone.
Sentiment: Negative
Polarity: -0.6

Review: Great ambiance and fast service!
Sentiment: Positive
Polarity: 0.85

Review: Meh, not bad but not great either.
Sentiment: Neutral
Polarity: 0.0

Review: Totally loved the dessert!
Sentiment: Positive
Polarity: 0.9
"""

# Save to local file
with open(filename, "w") as f:
    f.write(review_content)

# Upload to S3
s3 = boto3.client(
    "s3",
    aws_access_key_id=aws_access_key,
    aws_secret_access_key=aws_secret_key,
    region_name=aws_region
)

try:
    s3.upload_file(filename, bucket_name, filename)
    print(f"✅ Uploaded '{filename}' to S3 bucket '{bucket_name}'")
except Exception as e:
    print(f"❌ Upload failed: {e}")
