from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/")
async def root():
    return {"message": "Yengeç E-ticaret API Çalışıyor!"}

@app.post("/api/auth/login")
async def login(credentials: dict):
    # Mock login - gerçek auth burada olacak
    if credentials.get("email") == "test@yengec.co":
        return {"success": True, "message": "Giriş başarılı"}
    return {"success": False, "message": "Hatalı giriş"}

@app.get("/api/xml-sources")
async def get_xml_sources():
    # Mock XML kaynakları
    return [
        {
            "id": 1,
            "name": "Belle Vista Katalog",
            "url": "https://www.kargolat.com/export/...",
            "supplier": "Belle Vista",
            "status": "active",
            "productCount": 1245
        }
    ]
