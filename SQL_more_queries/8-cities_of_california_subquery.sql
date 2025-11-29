-- select
SELECT cities.id, states.name
FROM cities, states
WHERE states.name = 'California'
ORDER BY cities.id ASC;
