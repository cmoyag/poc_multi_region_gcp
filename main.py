from fastapi import FastAPI
import json
app = FastAPI()
 
@app.get("/")
def main():
   return {"status": "ok"}

@app.get("/region1")
def region1():
   data = {"status":"ok","region":"US-EAST-1"}
   return data

@app.get("/region2")
def region2():
   data = {"status":"ok","region":"US-CENTRAL-1"}
   return data