# Fahrplan Luzern - Engelberg (6:12, 7:12...)

for stunde in range(24):
	if stunde >= 6 and stunde <= 20:
		print(str(stunde) + ":12")

# oder

for stunde in range(6, 21):
	print(str(stunde) + ":12")