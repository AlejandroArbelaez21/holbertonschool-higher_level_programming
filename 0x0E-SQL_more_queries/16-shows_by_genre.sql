-- create and grants create a new user and set a privileges
-- create and grants create a new user and set a privileges
SELECT tv_shows.title, tv_genres.name FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_genres._id = tv_show.genre_id
ORDER BY tv_shows.title, tv_genres.name ASC;
