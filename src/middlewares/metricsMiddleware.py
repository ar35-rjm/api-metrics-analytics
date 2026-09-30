import time
import logging
import json
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request, Response

logging.basicConfig(filename='data/metrics.log', level=logging.INFO, format='%(asctime)s - %(message)s')

class MetricsMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()

        response: Response = await call_next(request)
        latency_ms = round((time.time() - start_time) * 1000, 2)

        metric_payload = {
            "method": request.method,
            "path": request.url.path,
            "status_code": response.status_code,
            "latency_ms": latency_ms,
            "client_ip": request.client.host if request.client else "127.0.0.1"
        }

        logging.info(json.dumps(metric_payload))
        return response