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


class InsertOneForm(QDialog):
    # NumGridRows = 3
    # NumButtons = 4

    def __init__(self):
        super(InsertOneForm, self).__init__()
        self.createFormGroupBox()
        self.temp_instance = None

        # buttonBox = QDialogButtonBox(QDialogButtonBox.Ok)
        # buttonBox.accepted.connect(self.accept)
        # buttonBox.rejected.connect(self.reject)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.formGroupBox)
        # mainLayout.addWidget(buttonBox)
        self.setLayout(mainLayout)

        self.setWindowTitle("Insert Data To The Table")

    def createFormGroupBox(self):
        self.formGroupBox = QGroupBox(
            "Populate the data needed for this table.")
        layout = QFormLayout()
        metadata_columns = ["a", "b", "c", "d"]

        collect_button = QPushButton(self, "Enter data")
        # TODO Srediti dugme i kupljenje podataka iz instanci koje se nalaze u ovom arrayu.
        self.input_array = []
        for column in metadata_columns:
            layout.addRow(QLabel(column),
                          self.append_instance(self.input_array))
        self.formGroupBox.setLayout(layout)
        layout.addRow(collect_button)

        collect_button.clicked.connect(self.process_input_fields)

    def append_instance(self, metadata_columns):
        metadata_columns.append(self.create_QLineEdit_Instance())
        return self.temp_instance

    def create_QLineEdit_Instance(self):
        self.temp_instance = QLineEdit()
        return self.temp_instance

    # TODO Srediti porovjeru i ispravnost podataka, ne smije biti prazan string itd...
    def process_input_fields(self):
        print("Button clicked...")
        for input in range(0, len(self.input_array)):
            print(self.input_array[input].displayText())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = InsertOneForm()
    sys.exit(dialog.exec_())
