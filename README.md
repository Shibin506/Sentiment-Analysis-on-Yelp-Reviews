**YelpReview: Real-Time Sentiment Analysis on Restaurant Reviews**

An end-to-end solution that streams Yelp reviews, performs real-time sentiment analysis using NLP techniques, and stores results in AWS S3 for further insights and visualization.
**
🔍 Overview**

YelpReview is a Python-based real-time sentiment classification pipeline. It ingests restaurant review text, classifies sentiment using TextBlob and VADER, and stores the labeled data in the cloud. This enables restaurant owners, marketers, and analysts to monitor customer sentiment instantly and take informed action.
**
 Challenge**

Yelp hosts millions of reviews, but businesses often struggle to analyze them efficiently in real-time. Manual analysis is time-consuming and not scalable. YelpReview automates this process with socket-based streaming and lightweight cloud storage, offering actionable sentiment metrics instantly.

** Key Features**

🧾 Streaming Reviews: Ingests review text using socket programming (or Apache NiFi)

🧠 Sentiment Classification: Uses TextBlob and VADER to classify sentiment as Positive, Negative, or Neutral

🔗 Modular Architecture: Clean Python scripts for ingestion, processing, and storage

☁️ Cloud Upload: Uploads results to AWS S3 using boto3

📊 Dashboard Ready: Output is dashboard-compatible for tools like Streamlit

**System Architecture**

java
Copy
Edit
Client Script (send_reviews.py)
      ↓
Socket Server (socket_server.py)
      ↓
Sentiment Analyzer (sentiment_analysis.py)
      ↓
Result Handler (upload_to_s3.py)
      ↓
AWS S3
🔄 ETL Workflow
🧪 Extract
Source: yelp_reviews.txt or live review input

Script: send_reviews.py


**Project Structure**

bash
Copy
Edit
YELPREVIEW/
├── app.py                   # App launcher (if needed)
├── main.py                  # Coordinates socket + sentiment + upload
├── socket_server.py         # Receives review stream
├── send_reviews.py          # Sends review lines
├── sentiment_analysis.py    # Applies TextBlob & VADER sentiment
├── upload_to_s3.py          # Uploads result to S3
├── yelp_reviews.txt         # Sample review input
├── test_env.py              # .env variable test
└── .env                     # AWS credentials

**Future Roadmap**

Replace socket with Apache NiFi for scalable ingestion

Add Streamlit dashboard for live sentiment monitoring

Store results in Redshift / Athena for analytics

Integrate Slack alerts for negative reviews


**Acknowledgements**

TextBlob

VADER Sentiment

Yelp Dataset

AWS S3

**Contributions**

Open to contributions! Feel free to fork the repo and raise a PR.

