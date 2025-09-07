[Module4_Proyecto SQL.sql](https://github.com/user-attachments/files/22198190/Module4_Proyecto.SQL.sql)
--1.Crea el esquema de la BBDD.
--2.Muestra los nombres de todas las películas con una clasificación por edades de ‘Rʼ
select film_id, title, release_year
from film
order by release_year;

--3. Encuentra los nombres de los actores que tengan un “actor_idˮ entre 30 y 40.
select *
from actor
where actor_id >= '30' and actor_id <= '40';

--4. Obtén las películas cuyo idioma coincide con el idioma original.
--Respuesta: La BBDD tiene valores nulos en lenguage orginal, por lo que no se puede realizar esta consulta. No obstante, se haría d ela siguiente manera: 

select film_id, title, l.language_id, f.original_language_id, l."name" as Lenguage
from film as f
inner join "language" as l 
on "f"."language_id"="l"."language_id"
where l.language_id=f.original_language_id;

SELECT *
FROM film
WHERE original_language_id IS NOT NULL AND language_id = original_language_id;

--5. Ordena las películas por duración de forma ascendente.

select title, length as Duración
from film
order by length asc;

--6. Encuentra el nombre y apellido de los actores que tengan ‘Allenʼ en su apellido.

SELECT first_name as nombre, last_name as apellido
FROM actor
WHERE "last_name" = 'ALLEN';

--7. Encuentra la cantidad total de películas en cada clasificación de la tabla “filmˮ y muestra la clasificación junto con el recuento.


SELECT c."name", count(f.film_id)
FROM film AS f
INNER JOIN film_category AS fc
    ON f.film_id = fc.film_id
INNER JOIN category AS c
    ON fc.category_id = c.category_id
group by c."name";

--8.Encuentra el título de todas las películas que son ‘PG-13ʼ o tienen una duración mayor a 3 horas en la tabla film.

select title, length as Duración, rating as PG_13
from film
where film.length>'3'and rating='PG-13'
order by film.length asc;

--9.Encuentra la variabilidad de lo que costaría reemplazar las películas.

select VARIANCE(replacement_cost) as variabilidad_reemplazo
from film f;

--10. Encuentra la mayor y menor duración de una película de nuestra BBDD.

select max (length), min (length)
from film f; 

--11.Encuentra lo que costó el antepenúltimo alquiler ordenado por día.

select *
from rental r
inner join payment p 
ON r."rental_id"=p."rental_id"
order by rental_date desc;

--12.Encuentra el título de las películas en la tabla “filmˮ que no sean ni ‘NC-17ʼ ni ‘Gʼ en cuanto a su clasificación.

select title, rating  
from film
where rating <> 'NC-17' and rating <> 'G';

--13. Encuentra el promedio de duración de las películas para cada clasificación de la tabla film y muestra la clasificación junto con el promedio de duración.

SELECT c."name" as categoria, round(AVG(f.film_id),2) as promedio_duracion
FROM film AS f
INNER JOIN film_category AS fc
    ON f.film_id = fc.film_id
INNER JOIN category AS c
    ON fc.category_id = c.category_id
group by c."name";

--14. Encuentra el título de todas las películas que tengan una duración mayor a 180 minutos.

select title as titulo_pelicula, length as duracion
from film f
where length > '180';

--15. ¿Cuánto dinero ha generado en total la empresa?

select sum(amount)
from payment;

--16. Muestra los 10 clientes con mayor valor de id.

select *
from customer c 
order by customer_id desc 
limit 10;

--17. Encuentra el nombre y apellido de los actores que aparecen en la película con título ‘Egg Igbyʼ.

select CONCAT(a.first_name,' ',a.last_name) as nombre_apellido, f.title 
from film f 
inner join film_actor fa 
on f.film_id =fa.film_id 
inner join actor a
on fa.actor_id =a.actor_id
where title='EGG IGBY';

--18. Selecciona todos los nombres de las películas únicos.

select distinct title 
from film f ;

--19.Encuentra el título de las películas que son comedias y tienen una duración mayor a 180 minutos en la tabla “filmˮ.

select f.title , c."name" , f.length 
from film f
INNER JOIN film_category AS fc
    ON f.film_id = fc.film_id
INNER JOIN category AS c
    ON fc.category_id = c.category_id
   where c."name" = 'Comedy' and f.length > '180';
  
 --20. Encuentra las categorías de películas que tienen un promedio de duración superior a 110 minutos y muestra el nombre de la categoría junto con el promedio de duración.
  
  select c."name", round(avg(f.length),2)
from film f
INNER JOIN film_category AS fc
    ON f.film_id = fc.film_id
INNER JOIN category AS c
    ON fc.category_id = c.category_id
 group by c."name" 
having avg(f.length)>'110';

--21.¿Cuál es la media de duración del alquiler de las películas?

select avg(rental_duration) as duracion_alquiler
from film f ;

--22.Crea una columna con el nombre y apellidos de todos los actores y actrices.

select concat(first_name, ' ',last_name) as nombre_apellidos
from actor a ;

--23. Números de alquiler por día, ordenados por cantidad de alquiler de forma descendente.

select rental_date , count(rental_id)
from rental
group by rental_date
order by date(rental_date) desc;

--24.Encuentra las películas con una duración superior al promedio.


SELECT title, length
FROM film
WHERE length > (SELECT AVG(length) FROM film);

--25.Averigua el número de alquileres registrados por mes. 


SELECT EXTRACT(MONTH FROM rental_date) AS mes, COUNT(*) AS total_alquileres
FROM rental r 
GROUP BY mes
ORDER BY mes;

--26. Encuentra el promedio, la desviación estándar y varianza del total pagado.

select avg(amount) as promedio, stddev(amount) as desviacion_estandar, variance(amount) as varianza 
from payment p ;

--27. ¿Qué películas se alquilan por encima del precio medio?


SELECT f.title, p.amount 
FROM payment p
INNER JOIN rental r ON p.rental_id = r.rental_id 
INNER JOIN inventory i ON i.inventory_id = r.inventory_id 
INNER JOIN film f ON f.film_id = i.film_id 
WHERE p.amount > (SELECT AVG(amount) FROM payment);

--28. Muestra el id de los actores que hayan participado en más de 40 películas.

 select a.actor_id  as actor_id ,count(f.film_id)
from film f 
inner join film_actor fa 
on f.film_id =fa.film_id 
inner join actor a
on fa.actor_id =a.actor_id
group by a.actor_id
having count(f.film_id) > '40';

--29.Obtener todas las películas y, si están disponibles en el inventario, mostrar la cantidad disponible.

 select count(i.inventory_id)
from film f 
inner join inventory i 
on f.film_id =i.film_id
group by film_id ;

--30.Obtener los actores y el número de películas en las que ha actuado.

select concat(a.first_name,' ',a.last_name) as nombre_completo, count(f.film_id)
from film f 
inner join film_actor fa 
on f.film_id =fa.film_id 
inner join actor a
on fa.actor_id =a.actor_id
group by a.actor_id;

--31.Obtener todas las películas y mostrar los actores que han actuado en ellas, incluso si algunas películas no tienen actores asociados.

select f.title as titulo, concat(a.first_name,' ',a.last_name) as nombre_completo
from film f 
full join film_actor fa 
on f.film_id =fa.film_id 
inner join actor a
on fa.actor_id =a.actor_id
order by f.title;

--32.Obtener todos los actores y mostrar las películas en las que han actuado, incluso si algunos actores no han actuado en ninguna película.


select concat(a.first_name,' ',a.last_name) as nombre_completo, f.title as titulo
from film f 
full join film_actor fa 
on f.film_id =fa.film_id 
inner join actor a
on fa.actor_id =a.actor_id
order by "nombre_completo" ;

--33. Obtener todas las películas que tenemos y todos los registros de alquiler.

SELECT f.title, r.rental_id , r.inventory_id 
FROM film f
LEFT JOIN inventory i 
ON f.film_id = i.film_id
LEFT JOIN rental r 
ON i.inventory_id = r.inventory_id
order by F.title ;

--34. Encuentra los 5 clientes que más dinero se hayan gastado con nosotros.

select concat(c.first_name,' ',c.last_name) as cliente , p.amount as dinero_gastado
from customer c 
inner join rental r 
on c.customer_id =r.rental_id 
inner join payment p 
on r.rental_id =p.rental_id 
order by p.amount desc
limit 5;


--35. Selecciona todos los actores cuyo primer nombre es 'Johnny'.

select *
from actor a 
where first_name = 'JOHNNY';

--36. Renombra la columna “first_nameˮ como Nombre y “last_nameˮ como Apellido.

select first_name as Nombre, last_name as Apellido
from actor a 
where first_name = 'JOHNNY';

--37.Encuentra el ID del actor más bajo y más alto en la tabla actor.

select max(actor_id) as id_maximo, min(actor_id) as id_minimo
from actor a ;

--38.Cuenta cuántos actores hay en la tabla “actorˮ.

select count(actor_id) 
from actor a ;

--39. Selecciona todos los actores y ordénalos por apellido en orden ascendente.

select first_name as Nombre, last_name as Apellido 
from actor a 
order by last_name desc;

--40. Selecciona las primeras 5 películas de la tabla “filmˮ.

select  title 
from film f 
limit 5;

--41.Agrupa los actores por su nombre y cuenta cuántos actores tienen el mismo nombre. ¿Cuál es el nombre más repetido? Keneth

select first_name, count(actor_id) as numero_actores
from actor a 
group by first_name 
order by numero_actores desc;

--42.Encuentra todos los alquileres y los nombres de los clientes que los realizaron.

select concat(c.first_name,' ',c.last_name) as nombre_completo, rental_id
from rental r 
inner join customer c 
on r.customer_id =c.customer_id
order by nombre_completo;

--43.Muestra todos los clientes y sus alquileres si existen, incluyendo aquellos que no tienen alquileres.

SELECT 
    CONCAT(c.first_name, ' ', c.last_name) AS nombre_completo, r.rental_id 
    FROM customer c 
LEFT JOIN rental r
ON c.customer_id = r.customer_id;

--44.Realiza un CROSS JOIN entre las tablas film y category. ¿Aporta valor esta consulta? ¿Por qué? Deja después de la consulta la contestación. 

--No tiene sentido ya que me está generando una tabla en la que todas las películas estan relacionadas con todas las categorias
SELECT f.title , c."name" 
FROM film f
CROSS JOIN film_category fc
CROSS JOIN category c;

--45.Encuentra los actores que han participado en películas de la categoría 'Action'.

create view actor_category as
select CONCAT(a.first_name, ' ', a.last_name) as nombre_actor, c.name
from actor a 
inner join film_actor fa 
on a.actor_id =fa.actor_id 
inner join film f 
on f.film_id =fa.film_id 
inner join film_category fc 
on fc.film_id =f.film_id 
inner join category c 
on c.category_id =fc.category_id;

select *
from actor_category
where name='Action';

--46.Encuentra todos los actores que no han participado en películas.


SELECT CONCAT(a.first_name, ' ', a.last_name) AS nombre_actor
FROM actor a
LEFT JOIN film_actor fa ON a.actor_id = fa.actor_id
LEFT JOIN film f ON f.film_id = fa.film_id
WHERE f.title IS NULL;


SELECT COUNT(*) AS actores_sin_peliculas
FROM actor a
LEFT JOIN film_actor fa ON a.actor_id = fa.actor_id
LEFT JOIN film f ON f.film_id = fa.film_id
WHERE f.title IS NULL;

--47. Selecciona el nombre de los actores y la cantidad de películas en las que han participado.

SELECT concat(a.first_name,' ',a.last_name) as NOMBRE_ACTORES, count(F.film_id)
FROM actor a
LEFT JOIN film_actor fa ON a.actor_id = fa.actor_id
LEFT JOIN film f ON f.film_id = fa.film_id
group by concat(a.first_name,' ',a.last_name);

--48. Crea una vista llamada “actor_num_peliculasˮ que muestre los nombres de los actores y el número de películas en las que han participado

create view ACTOR_NUM_PELICULAS AS
SELECT concat(a.first_name,' ',a.last_name) as NOMBRE_ACTORES, count(F.film_id)
FROM actor a
LEFT JOIN film_actor fa ON a.actor_id = fa.actor_id
LEFT JOIN film f ON f.film_id = fa.film_id
group by concat(a.first_name,' ',a.last_name);

select *
from ACTOR_NUM_PELICULAS;

--49.Calcula el número total de alquileres realizados por cada cliente.

select concat(c.first_name,' ',c.last_name) as cliente , count(r.rental_id)
from customer c 
inner join rental r 
on c.customer_id =r.rental_id 
group by concat(c.first_name,' ',c.last_name);

--50. Calcula la duración total de las películas en la categoría 'Action'.

  select c."name", round(avg(f.length),2)
from film f
INNER JOIN film_category AS fc
    ON f.film_id = fc.film_id
INNER JOIN category AS c
    ON fc.category_id = c.category_id
 group by c."name" 
having c."name" ='Action';

--51.Crea una tabla temporal llamada “cliente_rentas_temporalˮ para almacenar el total de alquileres por cliente.

CREATE TEMPORARY TABLE cliente_rentas_temporal AS
SELECT 
    CONCAT(c.first_name, ' ', c.last_name) AS cliente, 
    COUNT(r.rental_id) AS total_alquileres
FROM customer c
INNER JOIN rental r ON c.customer_id = r.customer_id
GROUP BY c.customer_id, CONCAT(c.first_name, ' ', c.last_name);

--52. Crea una tabla temporal llamada “peliculas_alquiladasˮ que almacene las películas que han sido alquiladas al menos 10 veces.

CREATE TEMPORARY TABLE peliculas_alquiladas AS
SELECT f.title, COUNT(r.rental_id) AS alquileres
FROM film f
LEFT JOIN inventory i ON f.film_id = i.film_id
LEFT JOIN rental r ON i.inventory_id = r.inventory_id
GROUP BY f.film_id
HAVING COUNT(r.rental_id) >= 10
ORDER BY f.title;

select *
from peliculas_alquiladas;

--53. Encuentra el título de las películas que han sido alquiladas por el cliente con el nombre ‘Tammy Sandersʼ y que aún no se han devuelto. Ordena los resultados alfabéticamente por título de película.

select f.title , concat(c.first_name,' ',c.last_name), r.return_date 
from customer c 
left join rental r 
on c.customer_id =r.customer_id 
left join inventory i 
on i.inventory_id =r.inventory_id 
left join film f 
on f.film_id =i.film_id
where concat(c.first_name,' ',c.last_name)='TAMMY SANDERS' and r.return_date is NULL;


--54. Encuentra los nombres de los actores que han actuado en al menos una película que pertenece a la categoría ‘Sci-Fiʼ. Ordena los resultados alfabéticamente por apellido.


SELECT CONCAT(a.first_name, ' ', a.last_name) AS nombre_completo, 
       COUNT(f.film_id) AS numero_peliculas
FROM actor a
INNER JOIN film_actor fa ON a.actor_id = fa.actor_id
INNER JOIN film f ON f.film_id = fa.film_id
INNER JOIN film_category fc ON fc.film_id = f.film_id
INNER JOIN category c ON c.category_id = fc.category_id
WHERE c."name" = 'Sci-Fi' 
GROUP BY a.actor_id, a.first_name, a.last_name 
HAVING COUNT(f.film_id) > 1 
ORDER BY numero_peliculas DESC;

--55.Encuentra el nombre y apellido de los actores que han actuado en películas que se alquilaron después de que la película ‘Spartacus Cheaperʼ se alquilara por primera vez. Ordena los resultados alfabéticamente por apellido.

SELECT DISTINCT a.first_name, a.last_name
FROM actor a
INNER JOIN film_actor fa ON a.actor_id = fa.actor_id
INNER JOIN film f ON fa.film_id = f.film_id
INNER JOIN inventory i ON f.film_id = i.film_id
INNER JOIN rental r ON i.inventory_id = r.inventory_id
WHERE r.rental_date > (
    SELECT MIN(rental_date)
    FROM rental r2
    INNER JOIN inventory i2 ON r2.inventory_id = i2.inventory_id
    INNER JOIN film f2 ON i2.film_id = f2.film_id
    WHERE f2.title = 'Spartacus Cheaper'
)
ORDER BY a.last_name, a.first_name;

--56. Encuentra el nombre y apellido de los actores que no han actuado en ninguna película de la categoría ‘Musicʼ.

SELECT DISTINCT a.first_name, a.last_name
FROM actor a
WHERE a.actor_id NOT IN (
    SELECT DISTINCT fa.actor_id
    FROM film_actor fa
    INNER JOIN film_category fc ON fa.film_id = fc.film_id
    INNER JOIN category c ON fc.category_id = c.category_id
    WHERE c."name" = 'Music'
)
ORDER BY a.last_name, a.first_name;

--57. Encuentra el título de todas las películas que fueron alquiladas por más de 8 días.

SELECT DISTINCT f.title
FROM film f
INNER JOIN inventory i ON f.film_id = i.film_id
INNER JOIN rental r ON i.inventory_id = r.inventory_id
WHERE r.return_date IS NOT NULL
AND (r.return_date - r.rental_date) > 8
ORDER BY f.title;

--58. Encuentra el título de todas las películas que son de la misma categoría que ‘Animationʼ.

select c."name" , f.title 
from film f 
left JOIN film_category fc 
ON fc.film_id = f.film_id
left JOIN category c 
ON c.category_id = fc.category_id
where c."name" = 'Animation';
--Tambien podría hacerse así, llegamos al mismo resultado
SELECT DISTINCT f.title
FROM film f
INNER JOIN film_category fc ON f.film_id = fc.film_id
INNER JOIN category c ON c.category_id = fc.category_id
WHERE c.category_id IN (
  
    SELECT category_id 
    FROM category 
    WHERE name = 'Animation'
)
ORDER BY f.title;

--59.Encuentra los nombres de las películas que tienen la misma duración que la película con el título ‘Dancing Feverʼ. Ordena los resultados alfabéticamente por título de película. 

select title 
from film f 
where length = (
select length
from film f 
where title ='DANCING FEVER')
order by title;

--60.Encuentra los nombres de los clientes que han alquilado al menos 7 películas distintas. Ordena los resultados alfabéticamente por apellido.

SELECT DISTINCT c.first_name, c.last_name
FROM customer c
INNER JOIN rental r ON c.customer_id = r.customer_id
INNER JOIN inventory i ON r.inventory_id = i.inventory_id
INNER JOIN film f ON i.film_id = f.film_id
GROUP BY c.customer_id, c.first_name, c.last_name
HAVING COUNT(DISTINCT f.film_id) >= 7
ORDER BY c.last_name, c.first_name;

--61.Encuentra la cantidad total de películas alquiladas por categoría y muestra el nombre de la categoría junto con el recuento de alquileres.
select c.name as categoria, count(r.rental_id) as total_alquileres
from category c
inner join film_category fc on c.category_id = fc.category_id
inner join film f on fc.film_id = f.film_id
inner join inventory i on f.film_id = i.film_id
inner join rental r on i.inventory_id = r.inventory_id
group by c.name;

--62.Encuentra el número de películas por categoría estrenadas en 2006.

select c.name as categoria, count(f.film_id) as total_peliculas
from category c
inner join film_category fc on c.category_id = fc.category_id
inner join film f on fc.film_id = f.film_id
where f.release_year = 2006
group by c.name
order by total_peliculas desc;


--63. Obtén todas las combinaciones posibles de trabajadores con las tiendas que tenemos. 
select s.store_id, st.staff_id, st.first_name, st.last_name
from store s
cross join staff st
order by s.store_id, st.staff_id;



--64. Encuentra la cantidad total de películas alquiladas por cada cliente y muestra el ID del cliente, su nombre y apellido junto con la cantidad de películas alquiladas.

select c.customer_id, c.first_name, c.last_name, count(r.rental_id) as total_alquileres
from customer c
inner join rental r on c.customer_id = r.customer_id
group by c.customer_id, c.first_name, c.last_name
order by total_alquileres desc;

