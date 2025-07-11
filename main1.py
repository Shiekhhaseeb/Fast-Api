from fastapi import FastAPI  # out framework (on which we will build all API's)
from pydantic import BaseModel  # helps in validation, helps us define the structure and syntax of data that we send
from typing import List  # python Libraries

# firstly in FastAPI we make an app
app = FastAPI()

class Tea(BaseModel):  # ✅ Fixed semicolon to colon
    id: int
    name: str
    origin: str

teas: List[Tea] = []

@app.get("/")  # decorators = give superpower to our fxns
def read_root():  # method def./function
    return {"message": "Welcome to chai code"}

@app.get("/teas")
def get_teas():  # ✅ Fixed indentation
    return teas
#2. Make a CRED
@app.post("/teas")
def add_tea(tea: Tea):  # ✅ Fixed missing colon
    teas.append(tea)
    return tea

@app.put("/teas/{tea_id}")
def update_tea(tea_id: int, updated_tea: Tea):  # ✅ Fixed syntax
    for index, tea in enumerate(teas):
        if tea.id == tea_id:
            teas[index] = updated_tea
            return updated_tea
    return {"error": "Tea not found"}

@app.delete("/teas/{tea_id}")
def delete_tea(tea_id: int):
    for index, tea in enumerate(teas):
        if tea.id == tea_id:
            deleted = teas.pop(index)
            return deleted
    return {"error": "Tea not found"}
