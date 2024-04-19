from fastapi import FastAPI 
from fastapi.responses import HTMLResponse 

app = FastAPI() 

@app.get("/")
async def read_item(nm: str = "Recruto", msg: str = "Давай дружить"):
    return {"name" : nm, "message" : msg}