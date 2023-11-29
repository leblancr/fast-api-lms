from typing import List, Optional
import fastapi 
from pydantic import BaseModel

router = fastapi.APIRouter()


@router.get("/courses")
async def read_courses():
    return {"courses": []}


@router.post("/courses")
async def create_courses_api():
    return {"courses": []}


@router.get("/courses/{id}")
async def read_course():
    return {"courses": []}


@router.patch("/courses/{id}")
async def update_courses():
    return {"courses": []}


@router.delete("/courses/{id}")
async def delete_courses_api():
    return {"courses": []}


@router.get("/courses/{id}/sections")
async def read_course_sections(id: int):
    return {"courses": []}
