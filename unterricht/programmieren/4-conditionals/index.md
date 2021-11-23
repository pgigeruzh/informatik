---
title: Conditionals (if-elif-else) und Flussdiagramme
author: Peter Giger
...

# Dokumente

[Slides](slides.html)

[Gruppenarbeit Flussdiagramm](slides-gruppenarbeit-flussdiagramm.html)


# Hilfreiche Links

**Wichtig:** Verbringen sie nicht zu viel Zeit mit der Theorie. Stundenlang Videos schauen oder Texte lesen, wird sie nicht weiterbringen. Beim Programmieren geht es um das "Können" und nicht um das "Wissen". Deshalb empfehle ich ihnen, selber zu experimentieren und viel zu üben (z. B. mit den Aufträgen oder eigenen Ideen/Projekten).

Auf Wikipedia finden sie eine gute Zusammenfassung zum Thema [Flussdiagramm](https://de.wikipedia.org/wiki/Programmablaufplan). Auch hier gilt: "Versuchen sie es einfach". Erstellen sie doch einfach einmal ein Diagramm und fragen mich (oder MitschülerInnen), was ich davon halte. Wenn sie das Flussdiagramm digital erstellen wollen, empfehle ich Ihnen [draw.io](https://app.diagrams.net) (siehe "Flowchart").

Auf **Youtube** finden sie (teilweise) gute Erklärvideos zum Thema Python. Hier sind einige Beispiellinks zu den Themen [If-Anweisung](https://www.youtube.com/watch?v=b6KzYbM-Hvg) und [If-Elif-Else](https://www.youtube.com/watch?v=f3YdEdYSNdk).

Die Plattform **W3Schools** bietet sich als Nachschlagewerk an (in Englisch). Hier ist der Link zum Thema [Conditionals](https://www.w3schools.com/python/python_conditions.asp).

Auf der Website von **Sylvia Lange** finden sie noch weitere (gute) Übungsaufgaben. Hier sind die [Aufgaben](https://sylvialange.de/python/Programmieraufgaben.pdf) (7, 8, 9, 10, 11) und die Lösungen
[[7]](https://sylvialange.de/python/python3/verzweigung/Quader.py)
[[8]](https://sylvialange.de/python/python3/verzweigung/Rabatt.py)
[[9]](https://sylvialange.de/python/python3/verzweigung/Rueckgeld.py)
[[10]](https://sylvialange.de/python/python3/verzweigung/pqFormel.py)
[[11]](https://sylvialange.de/python/python3/verzweigung/BMI.py)
zum Thema Conditionals/Verzweigungen.


# Prüfungsvorbereitung

> Lösungsvorschlag Aufträge
> 
> [Lösungsvorschlag Login I](files/login_without_username.py)
>
> [Lösungsvorschlag Login II](files/login_with_username.py)
>
> [Lösungsvorschlag Login II Flussdiagramm](files/login_with_username.drawio.png)

> Was ist der Output von diesem Programm? Erstellen sie ein Flussdiagramm dazu.
> ```python
> x = "Hello"
> y = "Tom"
> 
> if x != "Hello":
>   y = "Tim"
> 
> else:
>   y = "Tina"
> 
> print(y)
> ```
> 
> [Lösungsvorschlag](files/prüfungsvorbereitung_1.drawio.png)

> Was ist der Output von diesem Programm? Erstellen Sie ein Flussdiagramm dazu.
> ```python
> x = 5
> 
> if x < 0:
>   print("a")
> 
> elif x > 0:
>   if x == 5:
>     print("b")
> 
>   print("c")
> 
> else:
>   print("d")
> ```
> 
> [Lösungsvorschlag](files/prüfungsvorbereitung_2.drawio.png)

> Erstellen sie ein Programm, welches Schweizer Noten in das [amerikanische Notensystem](https://gpacalculator.net/grade-conversion/switzerland/) umrechnet.
>
> |Schweiz|US|
> |:-------|--:|
> |5.5-6   | A |
> |4.5-5.4 | B |
> |4.0-4.4 | C |
> |<4      | F |
> 
> ![](images/gpa_calculator.png){ width=100% }
> 
> [Lösungsvorschlag](files/gpa_calculator.py)