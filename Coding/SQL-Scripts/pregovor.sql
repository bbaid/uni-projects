use ships;

select name, launched
from ships
where name = CLASS

---
use movies;

select title, year
from movie
where title like '%Star%' 
and title like '%Trek%'
order by year desc, title

---

select MOVIETITLE, movie.year
from STARSIN join movie on movietitle = movie.title
where STARNAME in (select name from moviestar where birthdate > 1970-01-01 and birthdate < 1989-01-01)
