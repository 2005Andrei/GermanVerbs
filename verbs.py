import sqlite3
import sys
from cs50 import SQL

db = SQL("sqlite:///verbs.db")

all = db.execute("select * from verbs")

lookup = input("Type in verb:\n")
try:
	str(lookup)
except ValueError:
	print("Type a string mf")
	sys.exit(1)	
verb = db.execute("select verb from verbs where verb like :verb", verb=lookup)
v2 = db.execute("select v2 from verbs where verb like :verb", verb=lookup)
v3 = db.execute("select v3 from verbs where verb like :verb", verb=lookup)
online = db.execute("select book from verbs where verb like :verb", verb=lookup)
trad = db.execute("select traducere from verbs where verb like :verb", verb=lookup)

if verb is None:
	print("Did not find a match mf")
	sys.exit(1)
else:
	print("\n")
	print("Verb        ", end='')
	print(" V2        ", end='')
	print(" V3        ", end='')
	print(" Online        ", end='')
	print(" Traducere       ")
	for i in range(60):
		print("=", end='')
	print("\n")
	print(verb[0]["verb"] + "   ", end='')
	print(v2[0]["v2"] + "   ", end='')
	print(v3[0]["v3"] + "   ", end='')
	print(online[0]["book"] + "   ", end='')
	print(trad[0]["traducere"])
	print("\n")
	sys.exit(0)
