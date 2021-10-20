noten = []

while True:
    note = float(input("Note hinzufügen: "))
    noten.append(note)

    # durchschnitt berechnen
    summe = 0
    n = len(noten)
    for note in noten:
        summe = summe + note
    durchschnitt = summe / n

    print("------------------------")
    print("Noten: " + str(noten))
    print("Durchschnitt: " + str(durchschnitt))
    print("------------------------")
    