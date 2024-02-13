from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    cust_name:str
    item_name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


app = FastAPI()


@app.post("/items/")
async def create_item(item: Item):
    total = item.price + item.tax
    print("Total amount payable: ",total)
    return item, f"Hello {item.cust_name} your total amount payable for the {item.item_name} is ${total}"

    

