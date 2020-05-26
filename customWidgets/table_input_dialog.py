# from PySide2.QtWidgets import QWidget, QInputDialog, QLineEdit, QLabel, QVBoxLayout


# class TableInputDialog(QWidget):
#     def __init__(self, parent, file_metadata_columns):
#         super().__init__(parent)
#         self.times_called = 0
#         self.mainLayout = QVBoxLayout()
#         for table_name in file_metadata_columns:
#             self.mainLayout.addWidget(QLabel("Insert: {}".format(table_name)))
#             self.mainLayout.addWidget(QLineEdit(self))
#         self.times_called += 1

#         self.setLayout(self.mainLayout)


from PySide2 import QtGui, QtCore
from PySide2.QtWidgets import *
import sys


class ArtikalForma(QDialog):
    # NumGridRows = 3
    # NumButtons = 4

    def __init__(self):
        super(ArtikalForma, self).__init__()
        self.createFormGroupBox()

        # buttonBox = QDialogButtonBox(QDialogButtonBox.Ok)
        # buttonBox.accepted.connect(self.accept)
        # buttonBox.rejected.connect(self.reject)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.formGroupBox)
        # mainLayout.addWidget(buttonBox)
        self.setLayout(mainLayout)

        self.setWindowTitle("Dodaj artikal")

    def createFormGroupBox(self):
        self.formGroupBox = QGroupBox("Dodaj artikal")
        layout = QFormLayout()

        naziv = QLineEdit()
        naziv.setFixedSize(200, 40)
        layout.addRow(QLabel("Naziv:"), naziv)

        jm = QLineEdit()
        jm.setFixedSize(200, 40)
        layout.addRow(QLabel("Jedinica mere:"), jm)

        cena = QSpinBox()
        cena.setSuffix(" din")
        cena.setFixedSize(200, 40)
        cena.setRange(1, 999999999)
        layout.addRow(QLabel("Cena:"), cena)

        pdv = QSpinBox()
        pdv.setSuffix(" %")
        pdv.setFixedSize(200, 40)
        pdv.setRange(1, 100)
        layout.addRow(QLabel("PDV:"), pdv)

        self.formGroupBox.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = ArtikalForma()
    sys.exit(dialog.exec_())
