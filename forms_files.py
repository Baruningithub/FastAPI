from fastapi import FastAPI, File, Form, UploadFile
from typing_extensions import Annotated

app = FastAPI()


@app.post("/files_forms/")
async def create_file(
    filea: Annotated[bytes, File()],
    fileb: Annotated[UploadFile, File()],
    token: Annotated[str, Form()]):

    return {
        "filea_size": len(filea),
        "fileb_content_type": fileb.content_type,
        "token": token
    }