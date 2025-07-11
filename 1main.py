from fastapi import FastAPI #out frame work(on which we will build all API's)
from pydantic import BaseModel#helps in validation,helps us define the structure and syntax of data that we send
from typing import List#python Libraries

#firstly in FastAPI we make an app
app = FastAPI()

class Tea(BaseModel);
id : int
name :str
origin:str


teas : List[Tea] =[]

@app.get("/")#decorators = give superpower to our fxns
def read_root(): #method def./function
    return {"message": "Welcome to chai code"}

@app.get("/teas")
    def get_teas() :
    return teas