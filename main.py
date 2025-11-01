from fastapi import FastAPI, Depends, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from typing import List
from models import Movie
from database import get_db, init_db
from pydantic import BaseModel
import os

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def read_root():
    return FileResponse(os.path.join("static", "index.html"))

class MovieBase(BaseModel):
    title: str
    description: str
    poster_url: str
    rating: float

class MovieCreate(MovieBase):
    pass

class MovieResponse(MovieBase):
    id: int

    class Config:
        orm_mode = True

@app.on_event("startup")
async def startup_event():
    init_db()

@app.get("/movies", response_model=List[MovieResponse])
def get_movies(db: Session = Depends(get_db)):
    movies = db.query(Movie).all()
    return movies

@app.get("/movies/{movie_id}", response_model=MovieResponse)
def get_movie(movie_id: int, db: Session = Depends(get_db)):
    movie = db.query(Movie).filter(Movie.id == movie_id).first()
    if movie is None:
        raise HTTPException(status_code=404, detail="Фильм не найден")
    return movie

ADMIN_PASSWORD = "kinoman2025"  # В реальном проекте храните пароль безопасно!

class AdminAction(BaseModel):
    password: str

class MovieUpdate(BaseModel):
    movie: MovieCreate
    password: str

@app.post("/movies", response_model=MovieResponse)
def create_movie(movie: MovieCreate, db: Session = Depends(get_db)):
    db_movie = Movie(**movie.dict())
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    return db_movie

@app.get("/movies/search/{query}", response_model=List[MovieResponse])
def search_movies(query: str, db: Session = Depends(get_db)):
    movies = db.query(Movie).filter(
        Movie.title.contains(query) | Movie.description.contains(query)
    ).all()
    return movies

@app.put("/movies/{movie_id}", response_model=MovieResponse)
def update_movie(movie_id: int, update_data: MovieUpdate, db: Session = Depends(get_db)):
    if update_data.password != ADMIN_PASSWORD:
        raise HTTPException(status_code=403, detail="Неверный пароль администратора")
    
    db_movie = db.query(Movie).filter(Movie.id == movie_id).first()
    if db_movie is None:
        raise HTTPException(status_code=404, detail="Фильм не найден")
    
    for key, value in update_data.movie.dict().items():
        setattr(db_movie, key, value)
    
    db.commit()
    db.refresh(db_movie)
    return db_movie

@app.delete("/movies/{movie_id}")
def delete_movie(movie_id: int, admin: AdminAction, db: Session = Depends(get_db)):
    if admin.password != ADMIN_PASSWORD:
        raise HTTPException(status_code=403, detail="Неверный пароль администратора")
    
    db_movie = db.query(Movie).filter(Movie.id == movie_id).first()
    if db_movie is None:
        raise HTTPException(status_code=404, detail="Фильм не найден")
    
    db.delete(db_movie)
    db.commit()
    return {"message": "Фильм успешно удален"}