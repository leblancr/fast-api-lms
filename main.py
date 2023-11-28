from typing import Optional, List
from fastapi import FastAPI, Path, Query
from pydantic import BaseModel

app = FastAPI(
    title="FastAPI LMS",
    description="LMS for managing student courses",
    version="0.0.1",
    contact={
        "name": "Rich",
        "email": "rkba001@proton.me",
    },
    license_info={
        "name": "MIT"
    }
)

users = []


class User(BaseModel):
    email: str
    is_active: bool
    bio: Optional[str]


# response_model is return type, list of User objects
@app.get("/users", response_model=List[User])
async def get_users():
    return users


@app.post("/users")
async def create_user(user: User):
    users.append(user)
    return "Success"


@app.get("/users/{id}")
async def get_user(
    id: int = Path(..., description="The id of the user you want to retrieve.", gt=2),
    q: str = Query(None, max_length=5)
):
    return {'user': users[id], 'query': q}
