from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field 
from typing import Optional

app = FastAPI()
app.title = "Mi Aplicacion con FastAPI"
app.version ="0.0.1"

class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length=5,max_length=15)
    overview: str = Field(min_length=15,max_length=50)
    year: int = Field(le=2022)
    rating: float = Field(ge=0,le=10)
    category:str = Field(min_length=5,max_length=15)

    class Config():
        schema_extra = {
            "example": {
                "id": 1,
                "title": "Mi Pelicula",
                "overview": "Esta es la descripcion de la pelicula",
                "year": 2022,
                "rating": 9.8,
                "category": "Acción"
            }
        }

movies = [
    {
        'id': 1,
        'title': 'Avatar',
        'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        'year': '2009',
        'rating': 7.8,
        'category': 'Acción'    
    },
    {
        'id': 2,
        'title': 'Avatar',
        'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        'year': '2009',
        'rating': 7.8,
        'category': 'Acción'    
    } 
]
@app.get('/',tags =['home'])
def mesage():
    return HTMLResponse('<h1>Hello world</h1>')
@app.get('/movies', tags =['movies'])
def get_movies():
    return movies
@app.get('/movies/{id}', tags =['movies'])
def get_movies(id : int):
    for item in movies:
        if item["id"] == id:
            return item
    return []
@app.get('/movies/', tags =['movies'])
def get_movies_by_category(category: str,year: int):
    return [item for item in movies if item['category'] == category]

'''
@app.post('/movies', tags =['movies'])
def create_movies(id:int = Body(), title: str = Body(), overview: str = Body(), year:int = Body(), rating: float = Body(), category:str = Body()):
    movies.append({
        "id" : id,
        "title": title,
        "overview": overview,
        "year" : year,
        "rating" : rating,
        "category" : category
    })
    return movies
'''
@app.post('/movies', tags =['movies'])
def create_movies(movie: Movie):
    movies.append(movie)
    return movies

'''
@app.put('/movies/{id}' , tags =['movies'])
def update_movie(id:int, title: str = Body(), overview: str = Body(), year:int = Body(), rating: float = Body(), category:str = Body()):
    for item in movies:
        if item["id"] == id:
            item['title'] = title,
            item['overview'] = overview,
            item['year'] = year,
            item['rating'] = rating,
            item['category'] = category,
            item['title'] = title
            return movies
'''
@app.put('/movies/{id}' , tags =['movies'])
def update_movie(id:int, movie: Movie):
    for item in movies:
        if item["id"] == id:
            item['title'] = movie.title
            item['overview'] = movie.overview
            item['year'] = movie.year
            item['rating'] = movie.rating
            item['category'] = movie.category
            item['title'] = movie.title
            return movies

@app.delete('/movies/{id}' , tags =['movies'])
def delete_movie(id:int):
        for item in movies:
            if item["id"] == id:
                movies.remove(item)
                return movies
            