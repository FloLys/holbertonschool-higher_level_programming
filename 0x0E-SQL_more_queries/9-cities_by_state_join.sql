-- List all cities in database hbtn_0d_usa displaying cities.id - cities.name - states.name
SELECT cities.id, cities.name, states.name
FROM cities, states
WHERE cities.state_id = states.id
ORDER BY id ASC;
