from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

@app.post("/echo")
async def echo(request: Request):
    try:
        data = await request.json()  
    except:
        data = {"error": "Niepoprawny JSON"}
    return JSONResponse(content=data)
