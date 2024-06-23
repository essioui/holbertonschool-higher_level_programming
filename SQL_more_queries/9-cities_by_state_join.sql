-- lists all cities contained in the database hbtn_0d_usa.
-- uses an INNER JOIN to combine data from the cities and states tables.
SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN states ON cities.state_id = states.id;
