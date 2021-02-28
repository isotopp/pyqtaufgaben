# PyQtAufgaben

Das Programm denkt sich 10 Rechenaufgaben mit einfacher Subtraktion oder Addition aus.
Es zeigt die Aufgabe an, und man kann dann eine Lösung eingeben.
Das Programm sagt einem dann, ob man damit richtig lag.

Nach 10 Aufgaben oder wenn man den "Quit" Knopf drückt beendet es sich.
Dabei wird ein Endergebnis angezeigt.

## Klassen

### Aufgabe

Die Klasse Aufgabe kann mit 

```python
  aufgabe = Ausgabe()
  aufgabe.ausdenken()
```

aufgerufen werden.

Sie generiert dann eine zufällige Aufgabe der Form `a+b` oder `a-b`.
Dabei ist a immer größer oder gleich b.

Die Felder `a`, `op` und `b` enthalten die Variablen `a` und `b` sowie den Operand `+` oder `-`.
Das Feld `loesung` enthält die korrekte Lösung.

Die Methode `pruefen(ergebnis: int)` prüft, ob das Ergebnis `ergebnis` korrekt ist.

#### Beispiel

```python
  aufgabe = Aufgabe()
  aufgabe.ausdenken()
  print(f"{aufgabe.a} {aufgabe.op} {aufgabe.b} =", end = None)
  loesung = input()
  if aufgabe.pruefen(int(loesung)):
    print("Das war richtig.")
  else:
    print("Leider nein, richtig wäre {aufgabe.loesung} gewesen.")
```

### Score

Die Klasse `Score` kann mit

```python
  score = Score()
```

aufgerufen werden und zählt dann gelöste aufgaben und korrekt gelöste aufgaben mit.

Die Zähler sind `score` (Korrekte Lösungen), 
`counter` (Anzahl der bearbeiteten Aufgaben)
und `target` (Anzahl der zu lösenden Aufgaben).

Die Methode `correct()` teilt mit, daß eine Aufgabe korrekt gelöst wurde.
Die Methode `incorrect()` teilt mit, daß eine Aufgabe inkorrekt gelöst wurde.
Die Methode `done()` sagt, ob genug Aufgaben gelöst werden sind.

#### Beispiel

```python
  from random import choice

  score = Score()
  while not score.done():
    if choice([False, True]):
      score.correct()
    else:
      score.incorrect()

  print(f"Von {score.counter} Aufgaben waren {score.score} richtig.")
```

### Ui

Diese Klasse lädt die Datei `aufgaben.ui` und malt das Qt5 Interface.

`quit_pressed()`:
  Das Programm wird beendet.
  Dabei wird ein Statusdialog mit dem Endergebnis angezeigt.
  Diese Methode wird aufgerufen, wenn man den `Quit` Button drückt oder genug Aufgaben bearbeitet wurden.

`auswerten()`:
  Die Methode liest das Eingabefeld aus und wandelt es in einen Integer um.
  Diese Eingabe wird mit der korrekten Lösung verglichen.
  Entsprechend dem Ergebnis werden die Score Zähler hochgestellt und
  die Hinweistexte für den Benutzer aktualisiert.
  Das Eingabefeld wird gelöscht, um es auf die nächste Eingabe vorzubereiten.

  Wenn genug Aufgaben bearbeitet worden sind, wird das Programm beendet.
  Ansonsten wird eine neue Aufgabe erzeugt.

`set_aufgabe`: Die Groupbox mit der Rechenaufgabe wird aktualisiert.

`set_statusbar`: Die Statuszeile unten im Fenster wird aktualisiert.

`alles_updaten`: Nacheinander werden set_aufgabe() und set_statusbar() aufgerufen.

`load_ui`: Die `aufgabe.ui` Datei wird geladen.
  In der Datei sind verschiedene Bedienelemente mit Namen enthalten.
  Diese werden mit findChild() gesucht und gemerkt, damit wir im Programm darauf zugreifen können.


