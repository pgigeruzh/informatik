note = float(input("Note eingeben: "))
nachricht = "Deine Note im amerikanischen System ist: "

if note >= 5.5:
  print(nachricht + "A")
elif note >= 4.5:
  print(nachricht + "B")
elif note >= 4:
  print(nachricht + "C")
else:
  print(nachricht + "F")