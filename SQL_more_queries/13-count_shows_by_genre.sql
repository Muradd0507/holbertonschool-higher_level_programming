-- Join
SELECT tv_genres.name, tv_show_genres.show_id
FROM tv_genres
RIGHT JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
ORDER BY tv_show_genres.show_id 
