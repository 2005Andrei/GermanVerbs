import sys
from cs50 import SQL

db = SQL("sqlite:///verbs.db")

#only the verbs that I have to learn not all of the verbs in the german language
#cmd0 = input(">_ ")
while True:
	cmd0 = input(">_ ")
	if cmd0 == "help":
		print("This is a command line programm which is a cheat sheet for german classes.")
		for i in range(50):
			print("=", end='')
		print()
		print("Type a german verb and see the results.")
		for i in range(50):
                        print("=", end='')
		print()
		print("To exit type: <exit>")
	elif cmd0 == "exit":
		sys.exit(1)
	else:
		verb = db.execute("select verb from verbs where verb like :verb", verb=cmd0)
		v2 = db.execute("select v2 from verbs where verb like :verb", verb=cmd0)
		v3 = db.execute("select v3 from verbs where verb like :verb", verb=cmd0)
		online = db.execute("select book from verbs where verb like :verb", verb=cmd0)
		trad = db.execute("select traducere from verbs where verb like :verb", verb=cmd0)

		print("\n")
		print("Verb        ", end='')
		print(" V2        ", end='')
		print(" V3        ", end='')
		print(" Online        ", end='')
		print(" Traducere       ")
		for i in range(60):
			print("=", end='')
		print("\n")
		try:
			print(verb[0]["verb"] + "   ", end='')
			print(v2[0]["v2"] + "   ", end='')
			print(v3[0]["v3"] + "   ", end='')
			print(online[0]["book"] + "   ", end='')
			print(trad[0]["traducere"])
			print()
		except IndexError:
			#Wrong Spelling
			#Imma improve this alg in the future eventually
			fl = cmd0[0]
			if fl == "a":
				verbs = db.execute("select verb from verbs where verb like 'a%'")
			if fl == "b":
                                verbs = db.execute("select verb from verbs where verb like 'b%'")
			if fl == "c":
                                verbs = db.execute("select verb from verbs where verb like 'c%'")
			if fl == "d":
                                verbs = db.execute("select verb from verbs where verb like 'd%'")
			if fl == "e":
                                verbs = db.execute("select verb from verbs where verb like 'e%'")
			if fl == "f":
                                verbs = db.execute("select verb from verbs where verb like 'f%'")
			if fl == "g":
                                verbs = db.execute("select verb from verbs where verb like 'g%'")
			if fl == "h":
                                verbs = db.execute("select verb from verbs where verb like 'h%'")
			if fl == "i":
                                verbs = db.execute("select verb from verbs where verb like 'i%'")
			if fl == "j":
                                verbs = db.execute("select verb from verbs where verb like 'j%'")
			if fl == "k":
                                verbs = db.execute("select verb from verbs where verb like 'k%'")
			if fl == "l":
                                verbs = db.execute("select verb from verbs where verb like 'l%'")
			if fl == "m":
                                verbs = db.execute("select verb from verbs where verb like 'm%'")
			if fl == "n":
                                verbs = db.execute("select verb from verbs where verb like 'n%'")
			if fl == "o":
                                verbs = db.execute("select verb from verbs where verb like 'o%'")
			if fl == "p":
                                verbs = db.execute("select verb from verbs where verb like 'p%'")
			if int(len(verbs)) < 1:
				print("No match mf!")
				#sys.exit(1)
				
			for i in range(len(verbs)):
				v2 = db.execute("select v2 from verbs where verb like :verb", verb=verbs[i]['verb'])
				v3 = db.execute("select v3 from verbs where verb like :verb", verb=verbs[i]['verb'])
				online = db.execute("select book from verbs where verb like :verb", verb=verbs[i]['verb'])
				trad = db.execute("select traducere from verbs where verb like :verb", verb=verbs[i]['verb'])
				print(verbs[i]["verb"] + "   ", end='')
				print(v2[0]["v2"] + "   ", end='')
				print(v3[0]["v3"] + "   ", end='')
				print(online[0]["book"] + "   ", end='')
				print(trad[0]["traducere"])
				for j in range(60):
					print("-", end='')
				print("\n")
