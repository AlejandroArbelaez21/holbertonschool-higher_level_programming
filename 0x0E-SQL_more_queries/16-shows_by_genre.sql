-- create and grants create a new user and set a privileges
-- create and grants create a new user and set a privileges
SELECT tv_shows.title, tv_genres.name FROM tv_shows
LEFT JOIN tv_genres ON tv_show_genres.show_id = tv_show_genres.genre_id
JOIN tv_show_genres ON tv_show_genres.show_id = tv_shows.id
ORDER BY tv_shows.title;