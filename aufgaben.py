from PyQt5 import QtWidgets, uic
import sys
from random import randint, choice


class Aufgabe:
    op: str = ""
    a: int = 0
    b: int = 0

    loesung: int = 0

    def ausdenken(self) -> None:
        self.op = choice(self.allops)
        self.a = randint(1, 11)
        self.b = randint(1, 11)
        if self.a < self.b:
            self.a, self.b = self.b, self.a

        if self.op == "+":
            self.loesung = self.a + self.b
        if self.op == "-":
            self.loesung = self.a - self.b

    def pruefen(self, loesung: int) -> bool:
        return self.loesung == loesung

    def __init__(self) -> None:
        self.allops = ["+", "-"]
        self.ausdenken()


class Score:
    score: int = 0
    counter: int = 0
    target: int = 10

    def correct(self) -> None:
        self.counter += 1
        self.score += 1

    def incorrect(self) -> None:
        self.counter += 1

    def done(self) -> bool:
        return self.counter >= self.target

    def __init__(self):
        self.score = 0
        self.counter = 0
        self.target = 10


class Ui(QtWidgets.QMainWindow):
    button_quit: QtWidgets.QPushButton

    group_aufgabe: QtWidgets.QGroupBox

    label_a: QtWidgets.QLabel
    label_b: QtWidgets.QLabel
    label_op: QtWidgets.QLabel
    button_loesen: QtWidgets.QPushButton
    feld_antwort: QtWidgets.QLineEdit

    label_richtig: QtWidgets.QLabel

    statusbar: QtWidgets.QStatusBar

    def quit_pressed(self) -> None:
        msg: QtWidgets.QMessageBox = QtWidgets.QMessageBox()
        msg.setText(
            f"Von {self.score.counter} Aufgaben waren {self.score.score} richtig."
        )
        msg.setWindowTitle("Endergebnis")
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.setDefaultButton(QtWidgets.QMessageBox.Ok)
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.exec()
        sys.exit(0)

    def load_ui(self) -> None:
        uic.loadUi("aufgaben.ui", self)

        self.button_quit = self.findChild(QtWidgets.QPushButton, "button_quit")
        self.button_quit.clicked.connect(self.quit_pressed)

        self.group_aufgabe = self.findChild(QtWidgets.QGroupBox, "group_aufgabe")

        self.label_a = self.findChild(QtWidgets.QLabel, "label_a")
        self.label_b = self.findChild(QtWidgets.QLabel, "label_b")
        self.label_op = self.findChild(QtWidgets.QLabel, "label_op")
        self.button_loesen = self.findChild(QtWidgets.QPushButton, "button_loesen")
        self.button_loesen.clicked.connect(self.auswerten)

        self.label_richtig = self.findChild(QtWidgets.QLabel, "label_richtig")

        self.statusbar = self.findChild(QtWidgets.QStatusBar, "statusbar")

        self.feld_antwort = self.findChild(QtWidgets.QLineEdit, "feld_antwort")

    def auswerten(self) -> None:
        loesung: int
        text: str

        text = self.feld_antwort.text()
        if text is None or text == "":
            return

        try:
            loesung = int(text)
        except ValueError:
            return

        print(f"auswerten: loesung={loesung}, aufgabe.loesung={self.aufgabe.loesung}")

        if self.aufgabe.pruefen(loesung):
            self.score.correct()
            ergebnis = f"Deine Lösung: {loesung}. Das war richtig."
        else:
            self.score.incorrect()
            ergebnis = f"Deine Lösung: {loesung}. Richtig wäre: {self.aufgabe.loesung}."

        self.label_richtig.setText(ergebnis)
        self.feld_antwort.setText("")
        self.alles_updaten()

        if self.score.done():
            self.quit_pressed()
        else:
            self.aufgabe.ausdenken()
            self.alles_updaten()

    def set_aufgabe(self) -> None:
        self.label_a.setText(str(self.aufgabe.a))
        self.label_op.setText(str(self.aufgabe.op))
        self.label_b.setText(str(self.aufgabe.b))

        title = f"Aufgabe {self.score.counter}/{self.score.target}"
        self.group_aufgabe.setTitle(title)

    def set_statusbar(self) -> None:
        status = f"Aufgabe {self.score.counter}/{self.score.target}, {self.score.score} richtig."
        self.statusbar.showMessage(status)

    def alles_updaten(self) -> None:
        self.set_statusbar()
        self.set_aufgabe()
        self.show()

    def __init__(self):
        super(Ui, self).__init__()
        self.score = Score()
        self.aufgabe = Aufgabe()

        self.load_ui()
        self.alles_updaten()


app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec()
