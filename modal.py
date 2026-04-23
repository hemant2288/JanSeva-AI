from transformers import pipeline

classifier = pipeline("text-classification", model="distilbert-base-uncased")

def classify_complaint(text):
    result = classifier(text)[0]['label']
    
    # simple mapping (customize later)
    if "electric" in text:
        return "Electricity"
    elif "water" in text:
        return "Water"
    elif "road" in text:
        return "Roads"
    elif "garbage" in text:
        return "Sanitation"
    else:
        return "Public Service"
