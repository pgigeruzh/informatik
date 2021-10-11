for i in range(0, 3):
    benutzer = input("Benutzername eingeben: ")
    passwort = input("Passwort eingeben: ")

    if benutzer == "tom":
        if passwort == "strudel123":
            print("Herzlich Willkommen")
            break
        else:
            print("Passwort nicht korrekt! Verbleibende Versuche: " + str(2 - i))
    else:
        print("Benutzer nicht gefunden! Verbleibende Versuche: " + str(2 - i))

    if i == 2:
        print("Zu viele Login-Versuche. Ihr Konto wurde aus Sicherheitsgründen gesperrt.")
