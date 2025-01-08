from fastapi import FastAPI
from app.api.v1.endpoints import predict, analytics

app = FastAPI()

app.include_router(predict.router, prefix="/v1/images", tags=["images"])
app.include_router(analytics.router, prefix="/v1/analytics", tags=["analytics"])


@app.get("/healthcheck")
async def healthcheck():
    return {"status": "healthy"}
