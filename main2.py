from fastapi import FastAPI

app = FastAPI()


@app.get("/users/{user_name}")
def greetings(user_name:str):
    return{"message":f"hello,{user_name}"}