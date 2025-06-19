import os
from dotenv import load_dotenv
load_dotenv()

print(os.getenv("AWS_BUCKET"))  # should print yelp-sentiment-data
