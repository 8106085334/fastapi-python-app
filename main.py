from typing import List
from uuid import uuid4
from fastapi import FastAPI
from models import Gender, Role, User

app = FastAPI()

@app.get("/")
async def root():
  return {"greeting":"Hello world"}

@app.get("/api/v1/users")
async def get_users():
  return db

@app.post("/api/v1/users")
async def create_user(user: User):
  db.append(user)
  return {"id": user.id}

db: List[User] = [
         User(
              id=uuid4(),
               first_name="Vinay",
                last_name="Bhandari",
                 gender=Gender.male,
                  roles=[Role.user],
                   ),
          User(
               id=uuid4(),
                first_name="Shelly",
                 last_name="Bhandari",
                  gender=Gender.female,
                   roles=[Role.user],
                    ),
           User(
                id=uuid4(),
                 first_name="Ritu",
                  last_name="Bhandari",
                   gender=Gender.male,
                    roles=[Role.user],
                     ),
            User(
                 id=uuid4(),
                  first_name="AKC",
                   last_name="AKC",
                    gender=Gender.male,
                     roles=[Role.admin, Role.user],
                      ),
            ]
