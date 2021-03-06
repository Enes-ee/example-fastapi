from fastapi import Body, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .schemas import *
from .routers import post, user, auth, vote

# models.Base.metadata.create_all(bind=engine)

origins = ["https://www.google.com"]

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

# This fragment of code is not required. It is placed just for informational purposes.
@app.get("/")
def root():
    return {"message" : "root directory"}


