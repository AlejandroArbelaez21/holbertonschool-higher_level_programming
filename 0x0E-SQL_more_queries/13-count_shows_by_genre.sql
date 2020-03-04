-- create and grants create a new user and set a privileges
-- create and grants create a new user and set a privileges
SELECT tv_genres.name AS genre,
COUNT(tv_show_genres.genre_id) AS number_of_shows
FROM tv_genres
JOIN tv_show_genres
ON tv_show_genres.genre_id = tv_genres.id
GROUP BY genre
ORDER BY number_of_shows DESC;