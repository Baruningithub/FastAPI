from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel


class text(BaseModel):
    texts:str

usernames=[]
app = FastAPI()

#get
@app.get("/get_data/{data}")
async def get_data(data):
    return usernames

# put
@app.put("/put_data/{data}")
async def put_data(data):
    usernames.append(data)
    print(usernames)
    return usernames

#post
# @app.post("/post_data/{data}")
# async def post_data(data):
#     usernames.append(data)
#     print(usernames)
#     return usernames

#delete
@app.delete("/del_data/{data}")
async def del_data(data):
    if data not in usernames:
        return "Underflow"
    usernames.remove(data)
    print(usernames)
    return usernames