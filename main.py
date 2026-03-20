from fastapi import FastAPI,Form
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    email: str
    password: str

users = []

@app.get("/")
def home():
    return {"message": "Backend Running"}

@app.post("/sign-up")
def sign_up(email: str= Form(...,description="Enter your Email") , password:str= Form(...,description="Enter your Password")):
    user = User(email=email,password=password)

    #  Check if user already exists
    if any(u["email"] == user.email for u in users):
        return {"error": "User already exists"}

    #  Add new user
    users.append(user.dict())
    return {"message": "User created"}

@app.post("/login")
def login(email: str= Form(...,description="Enter your Email") , password:str= Form(...,description="Enter your Password")):
    user = User(email=email,password=password)

    for u in users:
        if u["email"] == user.email and u["password"] == user.password:
            return {"message": "Login successful"}
    return {"error": "Invalid"}




