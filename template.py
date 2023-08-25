from fastapi import FastAPI


app = FastAPI()

@app.get("/ip")
async def ip(ip: str):

    return {"ip":ip}





