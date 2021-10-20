def adresse_ausgeben(vorname, name, strasse, strassennr, plz, ort):
    print("--------------------")
    print(vorname + " " + name)
    print(strasse + " " + str(strassennr))
    print(str(plz) + " " + ort)
    print("--------------------")


adresse_ausgeben("Hans", "Mustermann", "Bahnhofstrasse", 16, 8000, "Zürich")
adresse_ausgeben("Hannah", "Musterfrau", "Nebenstrasse", 21, 3001, "Bern")
