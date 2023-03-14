from fastapi import FastAPI, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware

from app.workers import Worker

with open("README.md", "r") as file:
    next(file)
    description = file.read()

API = FastAPI(
    title="BackgroundTask API",
    version="0.0.1",
    docs_url="/",
    description=description,
)
API.worker = Worker()
API.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@API.get("/work", tags=["Work Ops"])
async def work(queue: BackgroundTasks):
    queue.add_task(API.worker)
    return "Job queued."
