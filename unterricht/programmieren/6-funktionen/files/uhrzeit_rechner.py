def uhrzeit_minuten_addieren(stunden, minuten, summand):
    print("--------------------------------")
    print("Uhrzeit: " + str(stunden) + " h " + str(minuten) + " min")
    print("Zu addierende Minuten: " + str(summand))

    for i in range(int(summand/60) + 1):

        if summand >= 60:
            # Zuerst die Stunden auffüllen
            summand = summand - 60
            stunden = stunden + 1
        elif (summand + minuten) >= 60:
            # Dann die Minuten wenn diese über 60 gehen
            stunden = stunden + 1
            minuten = minuten + summand - 60
        else:
            # Und zum Schluss nur die Minuten
            minuten = minuten + summand

        # Es gibt kein 24:00 aber 00:00
        if stunden >= 24:
            stunden = 0

    print("Neue Uhrzeit: " + str(stunden) + " h " + str(minuten) + " min")
    print("--------------------------------")


uhrzeit_minuten_addieren(16, 40, 0)
uhrzeit_minuten_addieren(16, 40, 20)
uhrzeit_minuten_addieren(16, 40, 200)
uhrzeit_minuten_addieren(16, 40, 2000)
uhrzeit_minuten_addieren(16, 10, 1111)
