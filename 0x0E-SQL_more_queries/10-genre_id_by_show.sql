-- inner join
SELECT tv_shows.title, tv_show_genres.genre_id
from tv_show_genres INNER JOIN tv_shows
on tv_show_genres.show_id = tv_shows.id;