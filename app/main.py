from fastapi import FastAPI, Request
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
        return {"status": "not ready"}
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
