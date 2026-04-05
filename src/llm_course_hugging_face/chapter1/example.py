import os
from transformers import pipeline

token = os.getenv("HF_TOKEN") or os.getenv("HUGGING_FACE_ACCESS_TOKEN")

classifier = pipeline(
    "sentiment-analysis",
    token=token,
)

print(classifier("I've been waiting for a Hugging Face course my whole life."))
