from typing import Union
import time
import asyncio

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    await asyncio.gather(*[duerme(), duerme(), duerme()])
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


async def duerme():
    print("duerme")
    await asyncio.sleep(5)
    print("despierta")
