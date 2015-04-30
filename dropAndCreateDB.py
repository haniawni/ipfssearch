import sqlite3

c = sqlite3.connect("hashes.db")
c.execute("drop table hashes")
c.execute("CREATE TABLE hashes (hash char(48) UNIQUE PRIMARY KEY, hits int not null, type varchar(30))")