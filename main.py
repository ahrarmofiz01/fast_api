from fastapi import FastAPI
app =FastAPI()
@app.get("/")
def Greet():
    return "Hello my name is ahrar mofiz!"
@app.get("/about")
def about():
    return 2**2

