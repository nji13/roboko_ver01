import mysql.connector

conn = mysql.connector.connect(host='localhost', user='root', password='', database='test_mysql_database')
curs = conn.cursor(buffered=True)

curs.execute(
    """
    DROP TABLE IF EXISTS posts
    """
)

curs.execute(
    """
    CREATE TABLE posts(
        id INT NOT NULL AUTO_INCREMENT,
        message VARCHAR(140),
        likes INT,
        area VARCHAR(20),
        PRIMARY KEY (id)
    )
    """
)

curs.execute(
    """
    INSERT INTO posts (message, likes, area) VALUES
        ('post-1', 12, 'Tokyo'),
        ('post-2', 8, 'Fukuoka'),
        ('post-3', 11, 'Tokyo'),
        ('post-4', 3, 'Osaka'),
        ('post-5', 8, 'Tokyo'),
        ('post-6', 9, 'Osaka'),
        ('post-7', 4, 'Tokyo'),
        ('post-8', 10, 'Osaka'),
        ('post-9', 31, 'Fukuoka')
    """
)
conn.commit()

curs.execute('SELECT * FROM posts')
for row in curs:
    print(row)

curs.close()
conn.close()