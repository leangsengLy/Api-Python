from fastapi import FastAPI,HTTPException,Depends
# from sqlalchemy.orm import Session
# import model,dataModel
app = FastAPI(debug=True)
@app.get("/")
def defaultHttp():
    return {"text":"Hello World"}