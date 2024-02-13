from fastapi import FastAPI
from typing import Union

app = FastAPI()

items = [{"item_name": "apple"}, {"item_name": "chocolate"}, {"item_name": "water"}]

# here we will declare function parmeters that are not part of path parameters which are interpreted as query paramteres  
@app.get("/items/")
async def read_item(start: int = 0, end: int = 3):
    return items[start : start+end]


# optional parameters
@app.get("/items/{item_id}")
async def read_item(item_id: str, q: Union[str, None] = None): # here q is the query string(optional)
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}


