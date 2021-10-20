# source: https://www.computerwoche.de/a/13-wirklich-wahre-it-geschichten,3218843

text = ["Einer", "der", "tödlichsten", "Angriffe", "auf", "amerikanische", "Soldaten",
        "während", "des", "ersten", "Golfkriegs", "1991", "entstand", "durch", "einen", "Programmierfehler", ".",
        "28", "Soldaten", "starben", ",", "als", "eine", "irakische", "Scud-Rakete", "Armee-Baracken", "in", "der",
        "Nähe", "von", "Dharan", "in", "Saudi-Arabien", "traf", ".", "Die", "in", "der", "Nähe", "stationierte",
        "Patriot-Raketenabschussrampe", "konnte", "die", "Scud", "nicht", "abfangen", ",", "weil", "sie", "einen",
        "Softwarebug", "aufwies", ":", "Ein", "Teil", "ihrer", "internen", "Berechnungen", "nutzte", "eine", "dezimale",
        "Ausgabe", "der", "Uhrzeit", "und", "ein", "anderer", "Teil", "eine", "binäre", ".", "Weil", "dieser", "Fehler",
        "in", "der", "internen", "Uhr", "der", "Patriot-Rakete", "auftrat", ",", "wurde", "das", "Missverhältnis", "immer",
        "größer", ",", "je", "länger", "das", "Raketensystem", "ohne", "Neustart", "blieb", ".", "Während", "des", "Kriegs",
        "waren", "die", "Raketensysteme", "nun", "aber", "in", "dauernder", "Bereitschaft", "und", "wurden", "niemals",
        "neu", "gestartet", ".", "Die", "Rakete", ",", "die", "Dharan", "traf", ",", "war", "die", "letzte", ",", "die",
        "der", "Irak", "während", "des", "Kriegs", "abfeuerte", "."]

summe = 0
for wort in text:
    if wort == "die":
        summe = summe + 1
    if wort == "Die":
        summe = summe + 1

print(summe)
