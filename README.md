# ipfssearch
Everything needed to run a search engine for IPFS

Have ipfs daemon running then:
	ipfs log tail | python ipfslogger.py

dropAndCreate.py creates hashes.db, which has table:
hashes:
	hash char(48) UNIQUE Primary Key
	count int not null
	extension varchar(30)