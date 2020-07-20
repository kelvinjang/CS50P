SELECT year, title, rating FROM movies
JOIN ratings ON movies.id = ratings.movie_id WHERE year = 2010 AND rating != "\N" ORDER BY rating DESC, title