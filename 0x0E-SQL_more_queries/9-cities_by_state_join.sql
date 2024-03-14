-- lists all cities contained in the database hbtn_0d_usa.
-- lists all rows in a particular column in database
SELECT cities.id, cities.name, states.name FROM cities LEFT JOIN states ON states.id = cities.states_id ORDER BY cities.id;