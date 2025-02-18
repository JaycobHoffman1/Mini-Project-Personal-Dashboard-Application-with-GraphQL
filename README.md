# Mini-Project: Movie Management API

- Author: Jaycob Hoffman

- Date: 17 February 2025

## Description

This project is a comprehensive API for managing movies within a MySQL database. It uses Flask, SQLAlchemy, and GraphQL to create an intuitive and flexible user experience while allowing users full control over the movies within the database.

## How to Run

When users first run the server, the following message will appear within their CLI:

![Alt text](images/running_application.png "Running Application")

Paste the link (http://127.0.0.1:5000) into your browser followed by "/graphql" to access the GraphQL interface.

## Features

- **Create Genre** (Note: users must create a genre before creating a movie)
![Alt text](create_genre.png "Create Genre")

- **Create Movie**
![Alt text](images/create_movie.png "Create Movie")

- **Query Genre**
![Alt text](images/query_genre.png "Query Genre")

- **Query Movie**
![Alt text](images/query_movie.png "Query Movie")

- **Update Genre**
![Alt text](images/update_genre.png "Update Genre")

- **Update Movie**
![Alt text](images/update_movie.png "Update Movie")

- **Get Genre by Movie**
![Alt text](images/get_genre_by_movie.png "Get Genre by Movie")

- **Get Movies by Genre**
![Alt text](images/get_movies_by_genre.png "Get Movies by Genre")

- **Delete Genre**
![Alt text](images/delete_genre.png "Delete Genre")

- **Delete Movie**
![Alt text](images/delete_movie.png "Delete Movie")

## Errors

Occasionally, when writing the mutation to delete a movie or genre, the following error will occur (example):

![Alt text](images/error.png "Error")

Solve this error by restarting the server and running the command again.

#

View the Movie Management API [GitHub Repository](https://github.com/JaycobHoffman1/module14-mini-project)