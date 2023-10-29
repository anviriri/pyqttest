from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
from random import randint

app = QApplication([])


WINDOW = QWidget()
WINDOW.resize(200, 100)

line = QVBoxLayout()

text = QLabel("Випадкове число:")
number = QLabel("?")
button = QPushButton("згенерувати")


line.addWidget(text)
line.addWidget(number)
line.addWidget(button)

WINDOW.setLayout(line)


def generate_rand():
    r = randint(0,100)
    number.setText(str(r))

button.clicked.connect(generate_rand)

























WINDOW.show()
app.exec()