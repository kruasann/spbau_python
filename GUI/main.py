from PyQt5 import uic
from PyQt5.QtWidgets import QApplication

import sys
import pathlib


Form, Window = uic.loadUiType("mainwindow.ui")
app = QApplication(sys.argv)
window = Window()
form = Form()

form.setupUi(window)
window.show()


def get_date():
    qdate = form.MyCalendar.selectedDate()
    return f'{qdate.day()}.{qdate.month()}.{qdate.year()}'


def get_note():
    return form.NewNote.toPlainText()


def create_file_note():
    note = get_note()
    date = get_date()
    path = f'{pathlib.Path.home()}/{date}.txt'

    file = open(path, "w")
    file.write(note)
    file.close()


form.AddNote.clicked.connect(create_file_note)

sys.exit(app.exec_())
