from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="MarketFlow", description="AI-powered marketing workflow builder")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "MarketFlow - AI-powered marketing workflow builder"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}