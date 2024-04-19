from fastapi import FastAPI, Request 
from fastapi.responses import HTMLResponse 
from fastapi.staticfiles import StaticFiles 
from fastapi.templating import Jinja2Templates 

app = FastAPI() 

templates = Jinja2Templates(directory = 'templates') 

@app.get("/", response_class = HTMLResponse)
async def read_item(request: Request, nm: str = "Recruto", msg: str = "Давай дружить"):
    return templates.TemplateResponse(
        request=request, 
        name="item.html", 
        context={"nm": nm, 'msg' : msg}
    )
