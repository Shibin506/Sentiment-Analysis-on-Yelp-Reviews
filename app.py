import streamlit as st
import boto3
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# AWS credentials
AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY")
AWS_REGION = os.getenv("AWS_REGION")
BUCKET_NAME = os.getenv("AWS_BUCKET")

# Initialize Streamlit page
st.set_page_config(page_title="Yelp Sentiment Dashboard", page_icon="📊")

# Title
st.markdown("## 📊 Yelp Sentiment Dashboard")
st.markdown("### 📁 Select Sentiment File from S3")

# Check credentials
if not BUCKET_NAME:
    st.error("⚠️ AWS_BUCKET not found. Check your .env file.")
else:
    st.success(f"✅ Loaded AWS_BUCKET: `{BUCKET_NAME}`")

    # Connect to S3
    s3 = boto3.client(
        "s3",
        aws_access_key_id=AWS_ACCESS_KEY,
        aws_secret_access_key=AWS_SECRET_KEY,
        region_name=AWS_REGION
    )

    # List files in bucket
    files = []
    response = s3.list_objects_v2(Bucket=BUCKET_NAME)
    for obj in response.get("Contents", []):
        files.append(obj["Key"])

    # Dropdown to select file
    selected_file = st.selectbox("Choose a sentiment file:", files)

    # If file selected
    if selected_file:
        file_obj = s3.get_object(Bucket=BUCKET_NAME, Key=selected_file)
        content = file_obj['Body'].read().decode("utf-8")

        # Extract individual reviews
        entries = content.strip().split("Review:")
        reviews_data = []
        for entry in entries[1:]:
            lines = entry.strip().splitlines()
            review_text = lines[0].strip()
            sentiment = polarity = ""
            for line in lines[1:]:
                if "Sentiment:" in line:
                    sentiment = line.split(":", 1)[1].strip()
                elif "Polarity:" in line:
                    polarity = line.split(":", 1)[1].strip()
            reviews_data.append({
                "text": review_text,
                "sentiment": sentiment,
                "polarity": polarity
            })

        # Dropdown to choose a review
        st.subheader("📂 Choose a review:")
        review_texts = [r["text"] for r in reviews_data]
        selected_review = st.selectbox("Select a review from file:", review_texts)

        if selected_review:
            review_details = next(r for r in reviews_data if r["text"] == selected_review)
            st.markdown("### 📝 Review Details")
            st.markdown(f"**📄 Text:** *{review_details['text']}*")

            sentiment_label = review_details['sentiment']
            emoji = "😄" if sentiment_label == "Positive" else "😞" if sentiment_label == "Negative" else "😐"
            st.markdown(f"**💬 Sentiment:** `{sentiment_label}` {emoji}")
            st.markdown(f"**📊 Polarity:** `{review_details['polarity']}`")
