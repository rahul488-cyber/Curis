from fastapi import FastAPI
import json

app = FastAPI()


@app.get("/result")
def result_send():
    with open('/Users/macromrit/Documents/Curis/medicine_chose.json', 'r') as jammer:
        data = json.load(jammer)
        return {'result' : data["medicine_chose"]}