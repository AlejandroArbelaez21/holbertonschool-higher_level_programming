-- create and grants create a new user and set a privileges
-- create and grants create a new user and set a privileges
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows JOIN tv_show_genres ON tv_show_genres.genre_id != NULL ORDER BY tv_show_genres.genre_id ASC;