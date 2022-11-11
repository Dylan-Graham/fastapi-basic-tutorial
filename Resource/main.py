from typing import Union

from fastapi import FastAPI

app = FastAPI()

########################################################################################################################################
# Get request                                                                                                                          #
########################################################################################################################################
@app.get("/")
def read_root():
    return {"Hello": "World from Resource folder"}

########################################################################################################################################
# Path parameters                                                                                                                      #
########################################################################################################################################
@app.get("/explorers/{explorer_id}")
async def getExplorer(explorer_id):
    return {"explore_id": explorer_id}


########################################################################################################################################
# Query parameters                                                                                                                     #
########################################################################################################################################
@app.get("/explorers")
async def getExplorer(limit: int = 4):
    explorers = ["Dylan", "Caryn", "Jeevan", "Kevin", "Riaan", "Simon", "Ockie", "Ricardo", "Vallan", "Jaen", "Shephard"]
    return explorers[:limit]

########################################################################################################################################
# Request body (import basemodel for type-checking, create type, create post endpoint, consume the new type in your endpoint)          #
########################################################################################################################################
from pydantic import BaseModel

class Explorer(BaseModel):
    name: str
    jobTitle: str

@app.post("/explorers/")
async def createExplorer(explorer: Explorer):
    return explorer