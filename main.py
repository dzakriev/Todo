from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse, RedirectResponse
import db_utils

app = FastAPI()
db_utils.init()

@app.get("/")
def redirect():
    return RedirectResponse("/docs")

@app.post("/items", status_code=201)
def add_item(title:str, description:str = None, completed:bool =  False):
    return db_utils.insert_item(title, description, completed)

@app.get("/items")
def get_items():
    return db_utils.get_items()
    
@app.get("/items/{item_id}")
def get_item(item_id:int):
    return db_utils.get_item(item_id)
    
@app.put("/items/{item_id}")
def update_item(item_id: int, title: str = None, description: str = None, completed: bool = None):
    data = {}
    if (title != None):
        data["title"] = title
    if (description != None):
        data["description"] = description
    if (completed != None):
        data["completed"] = completed
    if len(data) == 0:
        return HTTPException(400, detail="Provide item's fields.")
    
    result = db_utils.update_item(item_id, data)
    return JSONResponse(content={"message": f"Record {item_id} successfully updated."}) if result else HTTPException(404)

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    result = db_utils.delete_item(item_id)
    return JSONResponse(content={"message": "Deleted successfully."}) if result else HTTPException(404)
