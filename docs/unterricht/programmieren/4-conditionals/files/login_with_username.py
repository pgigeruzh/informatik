benutzer = input("Benutzername eingeben: ")
passwort = input("Passwort eingeben: ")

if benutzer == "tom":
    if passwort == "strudel123":
        print("Herzlich Willkommen")
    else:
        print("Passwort nicht korrekt")
else:
    print("Benutzer nicht gefunden")