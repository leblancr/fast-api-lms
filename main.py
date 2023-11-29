from fastapi import FastAPI

from api import users, courses, sections
from db.db_setup import engine
from db.models import user, course

# create all the tables associated with the declarative models defined in the
# user and course modules and bind them to the specified database engine
user.Base.metadata.create_all(bind=engine)
course.Base.metadata.create_all(bind=engine)

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
