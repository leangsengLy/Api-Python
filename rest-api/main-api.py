from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
app = FastAPI()

class Item(BaseModel):
    text:str 
    is_done : bool = False
    
items = []
@app.get("/")
def read_root():
    return {"text":"What are you doing now mrr leangseng"}

@app.post("/items/",response_model=Item)
def create_item(item: Item):
    items.append(item)
    return items

@app.get("/items/",response_model=list[Item])
def list_items(limit: int = 10):
    return items[0:limit]

@app.get("/items/get/{item_id}",response_model=Item)
def readItem(item_id:int)-> Item:
    if item_id >= len(items) or item_id < 0:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item": items[item_id]}
    
    