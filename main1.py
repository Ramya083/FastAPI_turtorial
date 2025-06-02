from fastapi import FastAPI

app = FastAPI()


@app.get("/users/")
def greet(name:str):
    return{"message":f"hello,{name}"}