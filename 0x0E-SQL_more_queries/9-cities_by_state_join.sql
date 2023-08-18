-- joining
SELECT cities.id, cities.name, states.name 
FROM states INNER JOIN cities
on states.id = cities.state_id
ORDER BY cities.id;