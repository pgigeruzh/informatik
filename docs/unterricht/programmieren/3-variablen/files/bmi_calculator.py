gewicht = input("Gib dein Gewicht in kg ein: ")
groesse = input("Gib deine Grösse in m ein: ")

bmi = int(gewicht) / (float(groesse) * float(groesse)) # or float(height) ** 2
print("Dein BMI ist: " + str(bmi))