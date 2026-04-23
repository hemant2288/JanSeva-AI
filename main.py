from fastapi import FastAPI
from fastapi .middleware.cors import CORSMiddleware
from database import save_complaint

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def classify(text):
    text = text.lower()
    if "bijli" in text or "electric" in text:
        return "Electricity"
    elif "water" in text or "pani" in text:
        return "Water"
    elif "road" in text:
        return "Roads"
    else:
        return "Public Service"

def priority(text):
    if "urgent" in text or "emergency" in text:
        return "High"
    return "Normal"

@app.post("/analyze")
def analyze(data: dict):
    text = data["complaint"]

    category = classify(text)
    pr = priority(text)

    result = {
        "complaint": text,
        "category": category,
        "priority": pr
    }

    save_complaint(result)

    return result
