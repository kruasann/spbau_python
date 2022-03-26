from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from mainwindow import *

import sys

Form, Window = uic.loadUiType("mainwindow.ui")
app = QApplication(sys.argv)
window = Window()
form = Form()
form.setupUi(window)
window.show()


def date_click(self):
    qdate = form.MyCalendar.selectedDate()
    date = f'{qdate.day()}.{qdate.month()}.{qdate.year()}'

    folder = "D:/MyNotes"
    global path, file
    path = f'{folder}/{date}.txt'
    file = open(path, "w")


def create_file_note(self):
    note = form.NewNote.toPlainText()
    file.write(note)
    file.close()


form.MyCalendar.clicked.connect(date_click)
form.AddNote.clicked.connect(create_file_note)

sys.exit(app.exec_())
