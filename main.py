from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from databases import Database
import sqlite3

app = FastAPI()

templates = Jinja2Templates(directory="templates")
with open('init.sql', 'r') as sql_file:
    sql_script = sql_file.read()
conn = sqlite3.connect('test1.db')
database = Database("sqlite:///test1.sqlite")
cur = conn.cursor()
cur.executescript(sql_script)
cur.close()
conn.close()

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    data = {
        "page": "Home page"}
    return templates.TemplateResponse("base.html", {"request": request, "data": data})
    

@app.get("/page/{page_name}", response_class=HTMLResponse)
def page(request: Request, page_name: str):
    data = {
        "page": page_name
    }
    return templates.TemplateResponse("base.html", {"request": request, "data": data})

#look up WSL2 python3 use file path
