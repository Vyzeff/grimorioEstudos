SELECT name FROM people WHERE id IN (SELECT person_id FROM directors WHERE movie_id IN (SELECT id FROM movies INNER JOIN ratings ON ratings.movie_id = movies.id WHERE rating > 9 OR rating = 9));

