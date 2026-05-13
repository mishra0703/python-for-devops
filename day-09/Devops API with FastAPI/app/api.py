from fastapi import FastAPI 
from routers import system_health,aws,logs


app = FastAPI(
    title="Internal DevOps Utilities API",
    description="This is an Internal API Utitlities App for Monitoring metrics, AWS Usage, Log Analysis, etc",
    version="1.1.0",
    doc_url="/docs",
    redoc_url="/redoc"
)


@app.get("/")
def home():
    return {"message" : "This is home page"}

app.include_router(system_health.router)
app.include_router(aws.router,prefix="/aws")
app.include_router(logs.router)