from fastapi import FastAPI

app = FastAPI()


@app.get("/query")
async def hello_query(id: str = None):
    return {"text": f"hello world, {id}!"}
