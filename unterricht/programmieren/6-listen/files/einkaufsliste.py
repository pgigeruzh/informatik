einkaufsliste = []

while True:
    artikel = input("Artikel hinzufügen: ")
    einkaufsliste.append(artikel)

    for e in einkaufsliste:
        print(" > " + e)