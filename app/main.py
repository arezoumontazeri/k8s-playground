from fastapi import FastAPI, Request, Response, status
import os
import socket
import time

app = FastAPI()

START_TIME = time.time()

@app.get("/healthz")
def healthz():
    return {"status": "ok"}

@app.get("/readyz")
def readyz():
    ready_flag = os.getenv("APP_READY", "true").lower()
    if ready_flag != "true":
        return Response(
            content='{"status":"not ready"}',
            media_type="application/json",
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
        )
    return {"status": "ready"}

@app.post("/echo")
async def echo(request: Request):
    body = await request.json()
    delay = float(os.getenv("RESPONSE_DELAY", "0"))
    if delay > 0:
        time.sleep(delay)
    return {
        "hostname": socket.gethostname(),
        "received": body,
        "app_mode": os.getenv("APP_MODE", "dev"),
        "model_name": os.getenv("MODEL_NAME", "fake-model")
    }

@app.get("/config")
def config():
    return {
        "APP_MODE": os.getenv("APP_MODE"),
        "MODEL_NAME": os.getenv("MODEL_NAME"),
        "RESPONSE_DELAY": os.getenv("RESPONSE_DELAY"),
    }

@app.get("/env")
def env():
    return {
        "hostname": socket.gethostname(),
        "api_key_exists": bool(os.getenv("API_KEY")),
        "uptime_seconds": int(time.time() - START_TIME),
    }

@app.get("/slow")
def slow():
    delay = float(os.getenv("RESPONSE_DELAY", "2"))
    time.sleep(delay)
    return {"status": "done", "delay": delay}

@app.post("/consume-memory")
def consume_memory(mb: int = 10):
    chunk = b"x" * (mb * 1024 * 1024)
    MEMORY_HOLDER.append(chunk)

    rss_mb = _get_rss_mb()

    return {
        "status": "allocated",
        "allocated_mb": mb,
        "chunks": len(MEMORY_HOLDER),
        "rss_mb": rss_mb,
    }


@app.post("/clear-memory")
def clear_memory():
    MEMORY_HOLDER.clear()

    return {
        "status": "cleared",
        "chunks": len(MEMORY_HOLDER),
        "rss_mb": _get_rss_mb(),
    }


@app.get("/metrics")
def metrics():
    return {
        "rss_mb": _get_rss_mb(),
        "chunks": len(MEMORY_HOLDER),
        "uptime_seconds": int(time.time() - START_TIME),
    }


def _get_rss_mb():
    try:
        with open("/proc/self/status", "r") as f:
            for line in f:
                if line.startswith("VmRSS:"):
                    parts = line.split()
                    kb = int(parts[1])
                    return round(kb / 1024, 2)
    except Exception:
        return None

    return None
