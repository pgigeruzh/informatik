# source: https://www.computerwoche.de/a/13-wirklich-wahre-it-geschichten,3218843

text = ["Lorem", "ipsum", "dolor", "sit", "amet", "consetetur", "sadipscing", "elitr", "lorem",
        "sed", "lorem", "diam", "nonumy", "eirmod", "tempor", "invidunt", "Lorem", "ut", "labore",
        "et", "dolore", "magna", "aliquyam", "erat", "sed", "diam", "voluptuz", "At", "lorem", 
        "vero", "eos", "et", "accusam", "et", "justo", "duo", "lorem", "dolores", "et", "ea"]

summe = 0
for wort in text:
    if wort == "lorem":
        summe = summe + 1
    if wort == "Lorem":
        summe = summe + 1

print(summe)
