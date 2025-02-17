import graphene
from models import Movie as MovieModel, Genre as GenreModel, db
from .movie_schema import AddMovie, UpdateMovie, DeleteMovie, Movie
from .genre_schema import AddGenre, UpdateGenre, DeleteGenre, Genre
from sqlalchemy.orm import Session

class Query(graphene.ObjectType):
    movies = graphene.List(Movie)
    genres = graphene.List(Genre)
    getMoviesByGenre = graphene.List(Movie, genreId=graphene.Int(required=True))
    getGenreByMovie = graphene.Field(Genre, movieId=graphene.Int(required=True))

    def resolve_getMoviesByGenre(self, info, genreId):
        return db.session.execute(db.select(MovieModel).where(MovieModel.genre_id == genreId)).scalars()
    
    def resolve_getGenreByMovie(self, info, movieId):
        movie = db.session.execute(db.select(MovieModel).where(MovieModel.id == movieId)).first()
        print(movie)
        return db.session.execute(db.select(GenreModel).where(GenreModel.id == movie.genre_id)).first()
    
    def resolve_movies(self, info):
        return db.session.execute(db.select(MovieModel)).scalars()

    def resolve_genres(self, info):
        return db.session.execute(db.select(GenreModel)).scalars()

class Mutation(graphene.ObjectType):
    create_movie = AddMovie.Field()
    update_movie = UpdateMovie.Field()
    delete_movie = DeleteMovie.Field()
    create_genre = AddGenre.Field()
    update_genre = UpdateGenre.Field()
    delete_genre = DeleteGenre.Field()