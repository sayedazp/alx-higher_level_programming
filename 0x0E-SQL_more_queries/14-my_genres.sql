-- count and join
SELECT tv_genres.name as name
from tv_show_genres INNER JOIN tv_shows
on tv_show_genres.show_id = tv_shows.id
INNER JOIN tv_genres
on tv_genres.id = tv_show_genres.genre_id
WHERE tv_shows.title = 'Dexter'
ORDER BY tv_genres.name;