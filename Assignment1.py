
import json
from fastapi import FastAPI
from pydantic import BaseModel
from random import randint

with open('test.json') as j_file:
    d=json.load(j_file)

class user_data(BaseModel):
    username:str
    email: str
    password: str

app = FastAPI()

@app.post("/create")
async def create(new_user:user_data):
    new_id = randint(1000,9999)
    # nl='\n'
    d[new_id] = dict(new_user)
    with open ('test.json','w+') as out:
        json.dump(d,out)
    return f"Dear {new_user.username} your account has been created Successfully! Your user id is {new_id}"

@app.get("/get/{user_id}")
async def get(user_id ):
    if user_id not in d.keys():
        return f"No user with user id {user_id}"
    return d[user_id]

@app.patch("/update/{user_id}")
async def update(user_id, user:user_data):
    if user_id not in d.keys():
        return f"No user with user id {user_id}"
    d[user_id] = dict(user)
    with open ('test.json','w+') as out:
        json.dump(d,out)
    return f"Dear {user_id} your details updated successfully"

@app.delete("/delete/{user_id}")
async def delete(user_id):
    if user_id not in d.keys():
        return f"No user with user id {user_id}"
    del d[user_id]
    with open ('test.json','w+') as out:
        json.dump(d,out)
    return f"Dear {user_id} your account deleted successfully"



