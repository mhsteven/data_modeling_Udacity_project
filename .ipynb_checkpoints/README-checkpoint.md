### Purpose
The purpose of this dataset is to provide easier way to explore data including songs and user activity on Sparkify's new music streaming app. Historically, these data are reside in JSON format in a directory, which is not easy to query, summarize, and perform analytical computation. Therefore, our approach here is to build an ETL pipeline to pull these JSON files into a SQL database. With this database, users can easily explore the data to understand their users better and more efficiently.  


### Database design
We build an ETL pipeline to pull all JSON log from the directory into Postgres database. We purposely build our database with **Star Schema** to optimize the query analysis since we know the objective of this database is to query for specific user activity log for analytical computation, and are likely to have multiple people access it paired with large amount of existing and new log activity pull in, so the simplicity of star schema is most suitable for this purpose. We have 2 datasets, the song dataset containing song and artist metadata such as title are artist name, and log dataset containing user activities including the timestamp they start to listen, the song they listen to, their gender and location etc. We split our dataset and build 5 tables to be our fact table and dimension tables as follows:
1. Fact table: 
    - songplays
2. Dimension table:
    - users
    - songs
    - artists
    - time


### How to use the files for ETL
1. run create_tables.py: this create the database and necessary tables following the star schema ready to be inserted.
2. run etl.py: this contain the automated code for ETL to pull from all JSON files in the directory and insert into our database to corresponding tables with necessary adjustment.
3. test.ipynb: you can use this jupyter notebook to run SQL query on our generated database.
4. sql_queries.py: (Optional) modify this if you want to further adjust the schema etc.
5. etl.ipynb: (Optional) you can use this for debugging purpose if you want to further modify your schema.


### Example queries and analysis

1. Top 5 most count of songplay by locations
```sql
SELECT location, count(*) 
FROM songplays 
GROUP BY location 
ORDER BY count(*) 
DESC LIMIT 5;
```

| location | count |
| ---------| -------|
|San Francisco-Oakland-Hayward, CA | 691 |
| Portland-South Portland, ME | 665 |
| Lansing-East Lansing, MI | 557 |
| Chicago-Naperville-Elgin, IL-IN-WI | 475 |
| Atlanta-Sandy Springs-Roswell, GA | 456 |


2. Count of songplay by gender and by level
```sql
SELECT songplays.level AS user_type, 
    COUNT(CASE WHEN users.gender = 'F' THEN 1 ELSE NULL END) AS Female_count, 
    COUNT(CASE WHEN users.gender = 'M' THEN 1 ELSE NULL END) AS Male_count 
    FROM songplays 
    JOIN users ON songplays.user_id = users.user_id 
    GROUP BY songplays.level;
```

|user_type | female_count | male_count |
| ---------| -------------| ----------|
| free | 593 | 636 |
| paid | 4294 | 1297 |


3. Count of songplay by weekday
```sql
SELECT time.weekday, 
    COUNT(songplays.songplay_id) AS number_of_play 
    FROM songplays 
    JOIN time ON songplays.start_time = time.start_time 
    GROUP BY time.weekday 
    ORDER BY weekday;
```

|weekday | number_of_play |
| ---------| -------------|
| 0 | 1014 |
| 1 | 1071 |
| 2 | 1364 |
| 3 | 1052 |
| 4 | 1295 |
| 5 | 628  |
| 6 | 396  |
