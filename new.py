from PyQt5.QtWidgets import (QApplication, QWidget,QLabel,
                                   QVBoxLayout, QHBoxLayout,
                                   QMessageBox,
                                   QRadioButton)
from PyQt5.QtCore import Qt

app = QApplication([])
window = QWidget()
window.resize(400,300)


main_line = QVBoxLayout()



H1 = QHBoxLayout()
H2 = QHBoxLayout()
H3 = QHBoxLayout()

question = QLabel("Яка зараз пора року?")
btn_answer = QRadioButton("Осінь")
btn_wrong1 = QRadioButton("Зима")
btn_wrong2 = QRadioButton("Весна")
btn_wrong3 = QRadioButton("Літо")

H1.addWidget(question, alignment=Qt.AlignCenter)

H2.addWidget(btn_wrong2, alignment=Qt.AlignCenter)
H2.addWidget(btn_wrong1, alignment=Qt.AlignCenter)

H3.addWidget(btn_answer, alignment=Qt.AlignCenter)
H3.addWidget(btn_wrong3, alignment=Qt.AlignCenter)

main_line.addLayout(H1)
main_line.addLayout(H2)
main_line.addLayout(H3)

window.setLayout(main_line)




def show_win():
    msg = QMessageBox()
    msg.setText("Правильно, ти виграв 3 грн!")
    msg.exec()

def show_lose():
    msg = QMessageBox()
    msg.setText("Неправильно, з тебе сотка!")
    msg.exec()

btn_answer.clicked.connect(show_win)

btn_wrong1.clicked.connect(show_lose)
btn_wrong2.clicked.connect(show_lose)
btn_wrong3.clicked.connect(show_lose)


window.show()
app.exec()