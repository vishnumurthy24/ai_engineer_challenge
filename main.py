
#FAST API 

#FIRST PROGRAM



from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Hello, AI Engineer!"}


# another get request

@app.get("/about")
def about():
    return {
        "project": "AI Assistant API",
        "version": "1.0"
    }


#Path Parameters

user_id = 101

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {
        "user_id": user_id
    }

#Query Parameters

@app.get("/search")
def search(name: str):
    return {
        "search_query": name
    }

@app.get("/products")
def products(category: str, limit: int = 10):
    return {
        "category": category,
        "limit": limit
    }