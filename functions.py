from fastapi import FastAPI

app = FastAPI()

@app.get("/square/{input}")
async def square(input : float):
    return input**2

@app.get("/cube/{input}")
async def cube(input : float):
    return input**3

@app.get("/pallindrome/{input}")
async def pallindrome(input):
    reverse = input[::-1]
    msg = "a" if (input==reverse) else "not a" 
    return f"reverse = {reverse} , hence {input} is {msg} pallindrome"