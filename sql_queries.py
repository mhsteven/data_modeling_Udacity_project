# DROP TABLES

songplay_table_drop = "DROP table IF EXISTS songplays;"
user_table_drop = "DROP table IF EXISTS users;"
song_table_drop = "DROP TABLE IF EXISTS songs;"
artist_table_drop = "DROP TABLE IF EXISTS artists;"
time_table_drop = "DROP TABLE IF EXISTS time;"

# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplays (songplay_id serial PRIMARY KEY, start_time timestamp NOT NULL, user_id int NOT NULL, level varchar, song_id varchar, artist_id varchar, session_id int, location varchar, user_agent varchar);
""")

user_table_create = ("""
CREATE TABLE IF NOT EXISTS users (user_id int PRIMARY KEY, first_name varchar NOT NULL, last_name varchar NOT NULL, gender char(1), level varchar);
""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS songs (song_id varchar PRIMARY KEY, title varchar NOT NULL, artist_id varchar NOT NULL, year int, duration numeric);
""")

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artists (artist_id varchar PRIMARY KEY, name varchar NOT NULL, location varchar, latitude numeric, longitude numeric)
""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS time (start_time timestamp PRIMARY KEY, hour int, day int, week int, month int, year int, weekday int)
""")

# INSERT RECORDS

songplay_table_insert = ("""
INSERT INTO songplays (songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) \
VALUES (DEFAULT,%s,%s,%s,%s,%s,%s,%s,%s)
""")

user_table_insert = ("""
INSERT INTO users VALUES (%s,%s,%s,%s,%s) \
ON CONFLICT ON CONSTRAINT users_pkey \
DO UPDATE SET level = excluded.level;
""")

song_table_insert = ("""
INSERT INTO songs VALUES (%s,%s,%s,%s,%s) \
ON CONFLICT ON CONSTRAINT songs_pkey \
DO NOTHING;
""")

artist_table_insert = ("""
INSERT INTO artists VALUES (%s,%s,%s,%s,%s) \
ON CONFLICT ON CONSTRAINT artists_pkey \
DO NOTHING;
""")


time_table_insert = ("""
INSERT INTO time (start_time, hour, day, week, month, year, weekday) \
VALUES ( %s,%s,%s,%s,%s,%s,%s) \
ON CONFLICT ON CONSTRAINT time_pkey \
DO NOTHING;
""")

# FIND SONGS

song_select = ("""
SELECT songs.song_id, songs.artist_id \
FROM songs \
JOIN artists ON songs.artist_id = artists.artist_id \
WHERE songs.title = %s AND artists.name = %s AND songs.duration = %s
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]