import sqlalchemy
from pprint import pprint

db = 'postgresql://Eleonora:1108@localhost:5432/Task3'
engine = sqlalchemy.create_engine(db)
connection = engine.connect()

res_1 = connection.execute("""
    SELECT album_name, year FROM albums
        WHERE year=2018;
        """).fetchmany(10)

res_2 = connection.execute("""
    SELECT title, time FROM tracks
        WHERE time = (SELECT MAX(time) FROM tracks)
            ORDER BY time DESC;
            """).fetchall()

res_3 = connection.execute("""
    SELECT title FROM tracks
        WHERE time >= 3;
            """).fetchall()

res_4 = connection.execute("""
    SELECT collection_name FROM collection
        WHERE year BETWEEN 2018 AND 2020;
            """).fetchall()

res_5 = connection.execute("""
    SELECT name FROM artist
        WHERE name NOT LIKE '%% %%';
            """).fetchall()

res_6 = connection.execute("""
    SELECT title FROM tracks
        WHERE title LIKE '%%You%%';
            """).fetchall()


if __name__ == '__main__':
    # pprint(engine)
    # pprint(connection)
    pprint(res_1)
    pprint(res_2)
    pprint(res_3)
    pprint(res_4)
    pprint(res_5)
    pprint(res_6)

