import sys
import time
import json
import sqlite3
conn = sqlite3.connect("hashes.db")
print "Hashcount:", conn.execute("SELECT count(*) from hashes")
k = 0
try:
    buff = ''
    while True:
        buff += sys.stdin.read(1)
        if buff.endswith('\n'):
        	q = json.loads(buff)
        	try:
        		wants = q['wants']
        		if wants != None:
        			for want in wants:
        				print want['Key']
        				try:
        					conn.execute('INSERT INTO hashes VALUES (\"' + want['Key'] + '\", 1, NULL)')
        				except sqlite3.IntegrityError:
        					conn.execute('UPDATE hashes SET hits = hits + 1 where hash = \"' + want['Key'] + '\"')
        	except KeyError:
        		pass
        	buff = ''
        	conn.commit()
        	k = k + 1
except KeyboardInterrupt:
	conn.commit()
	sys.stdout.flush()
	pass
print k