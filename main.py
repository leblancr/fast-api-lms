from fastapi import FastAPI
from api import users, courses, sections

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

app.include_router(users.router)
app.include_router(courses.router)
app.include_router(sections.router)
