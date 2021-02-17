import sys
from cs50 import SQL

db = SQL("sqlite:///verbs.db")

#only the verbs that I have to learn not all of the verbs in the german language
#cmd0 = input(">_ ")
while True:
	cmd0 = input(">_ ")
	if cmd0 == ".help":
		print("This is a command line programm which is a cheat sheet for german classes.")
		for i in range(50):
			print("=", end='')
		print()
		print("Type a german verb and see the results.")
		for i in range(50):
                        print("=", end='')
		print()
		print("To exit type: <.exit()>")
	elif cmd0 == ".exit()":
		sys.exit(1)
	else:
		try:
        		str(cmd0)
		except ValueError:
        		print("Type a string mf")
       			sys.exit(1)
		verb = db.execute("select verb from verbs where verb like :verb", verb=cmd0)
		v2 = db.execute("select v2 from verbs where verb like :verb", verb=cmd0)
		v3 = db.execute("select v3 from verbs where verb like :verb", verb=cmd0)
		online = db.execute("select book from verbs where verb like :verb", verb=cmd0)
		trad = db.execute("select traducere from verbs where verb like :verb", verb=cmd0)
		
		if verb != None:
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

		else: 
			#Wrong spelling 
			#I am going to improve this search alg eventually 
			firstLetter = cmd0[0] 
		#print("No matches found, I am going to give you a list of verbs starting wth that letter")
			print()
			verbs = db.execute("select verb from verbs where verb like ':verb%'", verb=cmd0[0])
			
			for verb in verbs:
				v2 = db.execute("select v2 from verbs where verb like :verb", verb=verb)
				v3 = db.execute("select v3 from verbs where verb like :verb", verb=verb)
				online = db.execute("select book from verbs where verb like :verb", verb=verb)
				trad = db.execute("select traducere from verbs where verb like :verb", verb=verb)
				print(verb[0]["verb"] + "   ", end='')
				print(v2[0]["v2"] + "   ", end='')
				print(v3[0]["v3"] + "   ", end='')
				print(online[0]["book"] + "   ", end='')
				print(trad[0]["traducere"])
				print("\n")
