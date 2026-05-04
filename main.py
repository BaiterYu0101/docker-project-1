from fastapi import FastAPI
import os 

#in here, the app act as an server, so whoever talk with the api, it will talking to this app object
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello to my Kubernetes World!"}

@app.get("/health")
def read_health():
    return {"status": "healthy"} #Here's using the Python dictionary to return a JSON response, which is a common practice in FastAPI. The key "status" has the value "healthy", indicating that the application is running properly.

@app.get("/crash")
def read_crash():
    os._exit(1)
