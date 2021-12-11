import sqlalchemy
from pprint import pprint

db = 'postgresql://Eleonora:1108@localhost:5432/S3'
engine = sqlalchemy.create_engine(db)
connection = engine.connect()

# res_1 = connection.execute("""
#     SELECT artistID FROM artists_genres;
#         """).fetchall()
#
# res_2 = connection.execute("""
#     SELECT title, time FROM tracks
#         WHERE time = (SELECT MAX(time) FROM tracks)
#             ORDER BY time DESC;
#             """).fetchall()
#
# res_3 = connection.execute("""
#     SELECT title FROM tracks
#         WHERE time >= 3;
#             """).fetchall()
#
# res_4 = connection.execute("""
#     SELECT collection_name FROM collections
#         WHERE release_year BETWEEN 2018 AND 2020;
#             """).fetchall()
#
# res_5 = connection.execute("""
#     SELECT name FROM artists
#         WHERE name NOT LIKE '%% %%';
#             """).fetchall()
#


res2_1 = connection.execute("""
    SELECT genre_name, COUNT(artistID) artists_q FROM genres g
    JOIN  artists_genres ag ON g.genreID = ag.artistID
    GROUP BY g.genre_name;
    """).fetchall()

res2_2 = connection.execute("""
    SELECT a.album_name, COUNT(t.trackID) FROM tracks t
    LEFT JOIN albums a ON t.albumID = a.albumID
    WHERE release_year BETWEEN 2019 AND 2020
    GROUP BY a.album_name;
            """).fetchall()

res2_3 = connection.execute("""
    SELECT a.album_name, AVG(t.time), COUNT(t.trackID) FROM tracks t
    LEFT JOIN albums a ON t.albumID = a.albumID
    GROUP BY a.album_name
    ORDER BY AVG(t.time);
            """).fetchall()

res2_4 = connection.execute("""
    SELECT ar.name FROM artists ar
    WHERE ar.name NOT IN (
        SELECT ar.name FROM artists ar
        LEFT JOIN artists_albums aa ON ar.artistID = aa.albumID
        LEFT JOIN albums aL ON al.albumID = aa.artistID
        WHERE al.release_year = 2020
        )
    ORDER BY ar.name;
            """).fetchall()

res2_5 = connection.execute("""
    SELECT collection_name FROM collections c
    LEFT JOIN tracks_collections tc ON c.collectionID = tc.trackID
    LEFT JOIN tracks t ON  tc.collectionID = t.trackID
    LEFT JOIN albums al ON t.albumID = al.albumID
    LEFT JOIN artists_albums aa ON al.albumID = aa.artistID
    LEFT JOIN artists ar ON aa.albumID = ar.artistID
    WHERE ar.name like '%%Miyagi%%'
    ORDER BY c.collection_name
            """).fetchall()

res2_6 = connection.execute(""" 
    SELECT al.album_name FROM albums al
    LEFT JOIN artists_albums aa ON al.albumID = aa.artistID
    LEFT JOIN artists ar ON aa.albumID = ar.artistID
    LEFT JOIN artists_genres ag ON ar.artistID = ag.genreID
    LEFT JOIN genres g ON ag.artistID = g.genreID
    GROUP BY al.album_name
    HAVING COUNT(distinct g.genre_name) > 1
    ORDER BY al.album_name;
        """).fetchall()

res2_7 = connection.execute("""
    SELECT t.title FROM tracks t
    LEFT JOIN tracks_collections tc ON t.trackID = tc.collectionID
    WHERE tc.trackID is null;
            """).fetchall()

res2_8 = connection.execute("""
    SELECT ar.name FROM artists ar
    LEFT JOIN artists_albums arl ON ar.artistID = arl.albumID 
    LEFT JOIN albums al ON arl.artistID = al.albumID 
    LEFT JOIN tracks t ON  al.albumID = t.albumID
    WHERE time = 
        (SELECT MIN(time) FROM tracks)
     ORDER BY time DESC;;
            """).fetchall()

res2_9 = connection.execute("""
    SELECT al.album_name  FROM albums al
    LEFT JOIN tracks t ON al.albumID = t.albumID
    WHERE t.albumID in (
        SELECT albumID
        FROM tracks
        GROUP BY albumID
        HAVING COUNT (trackID) = (
            SELECT count(trackID)
            FROM tracks
            GROUP BY albumID
            ORDER BY COUNT
            LIMIT 1
        )
    )
    ORDER BY al.album_name
            """).fetchall()

if __name__ == '__main__':
    # pprint(engine)
    # pprint(connection)
    # pprint(res2_1)
    # pprint(res2_2)
    # pprint(res2_3)
    # pprint(res2_4)
    # pprint(res2_6)
    # pprint(res2_7)
    # pprint(res2_8)
    pprint(res2_9)


