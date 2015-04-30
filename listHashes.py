import sqlite3

c = sqlite3.connect("hashes.db")
for r in c.execute("SELECT * from hashes order by hits DESC"):
	print r