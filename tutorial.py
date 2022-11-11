from typing import Union

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

# Path parameters
@app.get("/explorers/{explorer_id}")
async def getExplorer(explorer_id):
    return {"explore_id": explorer_id}

# Query parameters
@app.get("/explorers")
async def getExplorer(limit: int = 4):
    explorers = ["Dylan", "Caryn", "Jeevan", "Kevin", "Riaan", "Simon", "Ockie", "Ricardo", "Vallan", "Jaen", "Shephard"]
    return explorers[:limit]

# Bonus: Request body
from pydantic import BaseModel

class Explorer(BaseModel):
    name: str
    jobTitle: str

@app.post("/explorers/")
async def createExplorer(explorer: Explorer):
    # e.g. write code here to add the explorer to a database table...
    return explorer