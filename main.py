from fastapi import FastAPI
from src.middlewares.metricsMiddleware import MetricsMiddleware
from src.controllers.taskController import router as task_router
from src.controllers.healthCheckController import router as health_check_router

app = FastAPI(title="API Metrics & Logging Producer", version="1.0.0")
app = FastAPI(redirect_slashes=False)

app.add_middleware(MetricsMiddleware)
app.include_router(task_router)
app.include_router(health_check_router)

@app.get("/")
async def health_check():
    return {"status": "online"}