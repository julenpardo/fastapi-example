from fastapi import FastAPI
import uvicorn


app = FastAPI()


@app.get("/version")
async def version():
    return "0.0.1"


if __name__ == '__main__':
    uvicorn.run(app, port=8000, host="0.0.0.0")
