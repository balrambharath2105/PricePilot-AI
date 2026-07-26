from fastapi import FastAPI

app = FastAPI(
    title="PricePilot AI",
    description="AI-Powered Dynamic Pricing Optimization Platform",
    version="1.0.0",
)


@app.get("/", tags=["Home"])
async def root():
    return {
        "message": "Welcome to PricePilot AI 🚀",
        "status": "Backend Running Successfully",
        "version": "1.0.0"
    }


@app.get("/health", tags=["Health"])
async def health_check():
    return {
        "status": "healthy",
        "service": "PricePilot Backend"
    }