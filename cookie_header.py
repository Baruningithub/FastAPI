from typing import Union

from fastapi import Cookie, Header, FastAPI
from typing_extensions import Annotated

app = FastAPI()


# cookie parameter
@app.get("/cookie/")
async def read_items(ads_id: Annotated[Union[str, None], Cookie()] = None):
    return {"ads_id": ads_id}


# Header parameter
@app.get("/header/")
async def read_items(user_agent: Annotated[Union[str, None], Header()] = None):
    return {"User-Agent": user_agent}
