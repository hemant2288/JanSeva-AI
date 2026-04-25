from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from pymongo import MongoClient
import os

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ================= MongoDB Connection =================
MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017")

client = MongoClient(MONGO_URL)
db = client["janseva_ai"]
collection = db["complaints"]

# ================= Data Model =================
class Complaint(BaseModel):
    name: str
    issue: str
    category: str

# ================= Routes =================

# Home
@app.get("/")
def home():
    return {"message": "JanSeva AI Backend Running 🚀"}

# Test
@app.get("/test")
def test():
    return {"status": "Working fine"}

# Submit Complaint
@app.post("/submit")
def submit_complaint(data: Complaint):
    complaint = data.dict()
    collection.insert_one(complaint)
    return {"message": "Complaint submitted successfully"}

# Get All Complaints
@app.get("/complaints")
def get_complaints():
    data = list(collection.find({}, {"_id": 0}))
    return {"data": data}
