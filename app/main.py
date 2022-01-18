from fastapi import FastAPI


app = FastAPI()



@app.get("/")
async def root():
    return {"message": "Welcome To The CrossFit API"}


@app.get("/games/{year}")
async def games(year:int):
    return {"message": "It was the year of Thrusters"}