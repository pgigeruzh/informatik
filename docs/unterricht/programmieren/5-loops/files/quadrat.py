while True:
	zahl = input("Geben sie eine Zahl oder 'quit' ein: ")
	if zahl == "quit":
		break
	else:
		quadrat = int(zahl)*int(zahl)
		print(quadrat)