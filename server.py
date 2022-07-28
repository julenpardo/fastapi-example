from fastapi import FastAPI, Request
import json
import uvicorn


app = FastAPI()


@app.get("/version")
async def version():
    return "0.1.0"


@app.post("/flux-hook")
async def flux_hook(request: Request):
    print(json.dumps(await request.json(), indent=4))


if __name__ == '__main__':
    uvicorn.run(app, port=8000, host="0.0.0.0")
