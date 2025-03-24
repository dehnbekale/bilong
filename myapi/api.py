from fastapi import FastAPI
import json

app = FastAPI()

@app.get("/")
async def list_of_bilong():
    return {"message": "Hello World"}
@app.get("/{first_name}}")
async def get_bilong_id(first_name: str):
    with open("data.json", "r") as f:
        bilongs = json.load(f)
        print(bilongs)
        for bilong in bilongs:
            if bilong["first_name"] == first_name.title():
                return bilong
     