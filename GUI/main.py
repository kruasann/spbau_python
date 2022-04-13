import os
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication


class Note():
    def __init__(self):
        Form, Window = uic.loadUiType("mainwindow.ui")

        self.app = QApplication(sys.argv)
        self.window = Window()

        self.form = Form()
        self.form.setupUi(self.window)
        self.window.show()

        self.date = None
        self.note = None
        self.path = f'{os.path.abspath(os.curdir)}/Notes/'
        self.dir_path = f'{os.path.abspath(os.curdir)}/Notes/'

    def get_date(self):
        qdate = self.form.MyCalendar.selectedDate()
        return f'{qdate.day()}.{qdate.month()}.{qdate.year()}'

    def get_note(self):
        return self.form.NewNote.toPlainText()

    def create_file_note(self):
        self.note = self.get_note()
        self.date = self.get_date()
        self.path = f'{os.path.abspath(os.curdir)}/Notes/{self.date}.txt'
        self.form.Text.setText(f"Note {self.date} created!")
        file = open(self.path, "w")
        file.write(self.note)
        file.close()

    def delete_note(self):
        date = self.form.MyCalendar.selectedDate()
        date = f'{date.day()}.{date.month()}.{date.year()}.txt'
        if date in os.listdir(self.dir_path):
            os.remove(f'{self.dir_path}{date}')
            self.form.Text.setText(f"Note {date} deleted!")
        else:
            self.form.Text.setText(f"Note {date} doesn't exist!")


notes = Note()
notes.form.AddNote.clicked.connect(notes.create_file_note)
notes.form.DeleteNote.clicked.connect(notes.delete_note)

sys.exit(notes.app.exec_())
