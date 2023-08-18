-- count and join
SELECT tv_genres.name, count(tv_shows.id) AS number_of_shows
from tv_show_genres INNNER JOIN tv_shows
on tv_show_genres.show_id = tv_shows.id
INNER JOIN tv_genres
on tv_genres.id = tv_show_genres.genre_id
GROUP BY (tv_genres.id)
ORDER BY tv_shows.title, tv_show_genres.genre_id;