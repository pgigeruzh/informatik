---
title: Warum Python?
author: Peter Giger
---

# Lernziele <i class="fas fa-bullseye"></i>

> Sie verstehen den Unterschied zwischen Syntax und Semantik und können diesen anhand eines Beispiels in eigenen Worten beschreiben.

> Sie verstehen den Unterschied zwischen kompilierten und interpretierten Programmiersprachen und können jeweils einen Vor- und Nachteil aufzählen.

> Sie kennen den Unterschied zwischen Frontend und Backend und wissen, welche Geräte (Laptop, Server) jeweils gemeint sind.


# Warum Python <i class="fas fa-question"></i>

1. Einfacher Syntax
   
   ```python
   def foo(x):
      if x == 0:
         bar()
      else:
         foo(x - 1)
   ```

2. Findet fast überall Verwendung
   
   - IoT: Raspberry Pi ![](images/raspberry.jpg){ width=100px }
   - Machine Learning: Netflix ![](images/netflix.png){ width=50px }
   - Web App (Backend): Instagram ![](images/instagram.png){ width=50px }
   - Web App (Frontend): -


# Ein Beispielprojekt von mir: <br> Gleitschirm Leinenreissmaschine <i class="fas fa-parachute-box"></i>

||||
| ----------------------------------- | ----------------------------------- | ----------------------------------- |
| ![](images/line.jpg){ height=250px } | ![](images/machine.jpg){ height=250px } | ![](images/sensor.jpg){ height=250px } |
| ![](images/esp32.jpg){ height=250px } | ![](images/code.jpg){ height=250px } | <video src="images/movie.MOV" controls height="250px"></video> |


# Auftrag: In 3 Gruppen (ca. 15 Minuten) <i class="fas fa-users"></i>

- Gruppe 1: [Syntax vs. Semantik](https://gadget-info.com/difference-between-syntax)
- Gruppe 2: [Kompilierte vs. interpretierte Sprache](https://www.elektronik-kompendium.de/sites/com/1705231.htm)
- Gruppe 3: [Backend vs. Frontend](https://www.ironhack.com/de/webentwicklung/front-end-vs-back-end-unterschied)

Eine (zufällige) Person pro Gruppe präsentiert ihr Thema

::: notes
- Syntax vs. Semantik:
  Die Syntax sind die Zeichen (z. B. 1 + 2) und die Semantik die Bedeutung (z. B. 1 + 2 = 3, aber theoretisch wäre auch 1 + 2 = 12 möglich). Die Semantik ist in Programmiersprachen einfach überprüfbar (z. B Klammern vergessen), die Syntax hingegen nicht.
- Kompilierte vs. interpretierte Sprache: 
  Ein Kompiler generiert eie Datei mit Maschinencode (Bits bzw. LLVM), ein Interpreter führt die Instruktionen direkt aus. Interpretierte Programme sind generell langsamer aber schneller in der Entwicklung (kein warten aufs kompilieren).
- Backend vs. Frontend:
  Das Frontend läuft auf einem Client (Handy, Laptop...), das Backend auf einem Server z. B. Google-Server inkl. Datenbanken etc.
:::