-- joining
SELECT cities.id, cities.name, states.name 
FROM states INNER JOIN cities
on states.id = cities.id
ORDER BY cities.id;