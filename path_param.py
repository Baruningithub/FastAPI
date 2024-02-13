from fastapi import FastAPI

app = FastAPI()

# passing 'name' path as parameter to the function

@app.get("/hello/{name}")

async def index(name):
   return {"message": 'hello '+ name}

#path parameter with type
@app.get("/number/{digit}")

async def index(digit : int):
   return {"message": digit}

