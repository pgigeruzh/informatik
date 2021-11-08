---
title: Loops (while, for) und Flussdiagramme
author: Peter Giger
---

# Lernziele <i class="fas fa-bullseye"></i>

> Sie verstehen das Prinzip von Loops (while, for) und können dieses Wissen in einem Programm umsetzen

> Sie können ein Flussdiagramm aufgrund von Programmcode (oder vice verca) erstellen

# Was sind Loops? (Schleifen) <i class="fas fa-redo"></i>

Loops (Wiederholungen) kennen sie bereits aus ihrem Alltag, z. B. aus der [Musik](https://www.youtube.com/watch?v=C0jEJL-RdPo)

In Python gibt es zwei Arten von Loops, **While** und **For**:

```python
# (1) While-Loop

i = 0
while i < 5: # solange i < 5
  print("hallo", end=" ") # print ohne neue Zeile
  i = i + 1 # i um eins erhöhen

# Output: hallo hallo hallo hallo hallo
```

```python
# (2) For-Loop

for i in range(0, 5): # für jedes i von 0 bis 5
  print("hallo", end=" ") # print ohne neue Zeile

# Output: hallo hallo hallo hallo hallo
```

::: notes
:::


# While-Loops in Python <i class="fas fa-redo"></i>
While-Loops können alles, was For-Loops können und noch mehr. Trotzdem sollte man in den meisten Fällen For-Loops verwenden (weniger fehleranfällig).
```python
i = 5 # Zähler-Variable definieren
while i < 10:
  print(i, end=" ")
  i = i + 1 # Zähler-Variable erhöhen

# Output: 5 6 7 8 9
```
```python
while True: # Unendliche Schleife
  print("hallo")

# Output: hallo hallo hallo hallo hallo hallo hallo hallo ...
```

::: notes
- Vgl. Misra-C + Leserlichkeit
- Demo
:::


# For-Loops in Python <i class="fas fa-redo"></i>

For-Loops sind "Syntactic Sugar" für While-Loops, wobei die Funktion "range(von, bis)" notwendig ist. Die Zähler-Variable (z. B. i) iteriert dabei durch den "range".

```python
for i in range(5, 10):
  print(i, end=" ")

# Output: 5 6 7 8 9
```

Mit dem "break"-Befehl kann der Loop verlassen werden (funktioniert auch bei While-Loops)

```python
for i in range(5, 10):
  if i == 8:
    break # Loop verlassen
  print(i, end=" ")

# Output: 5 6 7
```

::: notes
- Demo
:::

# Das Flussdiagramm als visuelle Darstellung <i class="fas fa-chart-pie"></i>

![](images/flussdiagramm_while.drawio.png){ height=300px }

```python
i = 2
while i < 10:
  print(i)
  i = i + 2
print("fertig")

# Output: 2 4 6 8 fertig
```

<small>(Da For-Loops nur "Syntactic Sugar" für While-Loops sind, werden diese als While-Loop dargestellt.)</small>

::: notes
- Zeige Wikipedia
- Demo
:::

# Auftrag: Stellen sie sich vor, sie seien wieder in der Primarschule <i class="fas fa-school"></i>

![](images/primarschule.png){ height=130px }

1. Die Lehrerin möchte, dass sie die Zahlen von 1 bis 1000 aufschreiben. Automatisieren sie diesen Auftrag.

2. Die Lehrerin verlangt nun, dass sie von 1000 wieder rückwärts auf 1 zählen. Erstellen sie ein Programm.

3. Nun möchte die Lehrerin auch noch, dass sie die 7er-Reihe bis 1000 (1x7, 2x7, 3x7...) aufschreiben. Erstellen sie wieder ein Programm.

# Auftrag: Fahrplan Luzern - Engelberg <i class="fas fa-subway"></i>

Der IR (Interregio) von Luzern nach Engelberg fährt nur 1x pro Stunde. Der erste Zug fährt um 6:12 und der letzte Zug um 20:12. Erstellen sie ein Programm, welches den Fahrplan ausgibt (ohne jeden Zug einzeln aufzuschreiben).

|||
| ----------------------------------- | ----------------------------------- |
| ![](images/fahrplan.png){ height=400px } | ![](images/fahrplan_2.png){ height=400px } |


# Auftrag: Prüfungssoftware Programmieren <i class="fas fa-shoe-prints"></i>

(1) Programmieren sie eine Software, welche eine Frage stellt (z. B. Was ist die Hauptstadt der Schweiz?) und nach 10 falschen Antworten "Prüfung leider nicht bestanden" ausgibt. Wenn die Frage richtig beantwortet wird, soll "Gratulation!" ausgegeben werden. <br><br><small>Tipp: Mit "ctrl-c" brechen sie die Ausführung des Programms ab</small>

(2) Erstellen sie das Flussdiagramm dazu


|||
| ----------------------------------- | ----------------------------------- |
| ![](images/exam_software.png){ height=200px } | ![](images/exam_software_2.png){ height=70px } |

::: notes
:::