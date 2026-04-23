import re

def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9 ]', '', text)
    return text

def detect_priority(text):
    urgent_words = ["urgent", "emergency", "immediately", "danger"]
    for word in urgent_words:
        if word in text:
            return "High"
    return "Normal"
