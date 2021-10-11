for i in range(0, 10):
    antwort = input("Was ist die Hauptstadt der Schweiz? ")
    if antwort == "Bern":
        print("Gratulation, sie haben die Prüfung bestanden!")
        break
    elif i == 9:
        print("Sie haben die Prüfung leider nicht bestanden.")
    else:
        print("Leider Falsch, sie haben noch " + str(9 - i) + " Versuche")
