/* 	Write and save your SQL code in this file.
	Do not rename or move it.  */

select title, name
from movie
	join movie_actor
		on movie.id = movie_actor.movie_id
	join actor
		on actor.id = movie_actor.actor_id
order by title, name