from PySide2 import QtWidgets
from PySide2.QtCore import QAbstractTableModel
from data_classes.databse_file_handlers.serial_file_handler import SerialFileHandler
import pickle
from PySide2 import QtCore


class AbstractTableModel(QAbstractTableModel):
    def __init__(self, file_clicked):
        super().__init__()
        self.path_to_file_clicked = file_clicked
        self.binary_data_unpacked = None
        self.unbox_data_from_clicked_file()
        # self.print_unpacked_data()
        self.file_handler = SerialFileHandler(
            self.original_data_filepath, self.original_metadata_filepath) if self.database_type == "serial" else 0
        self.data = self.file_handler.get_all()
        self.print_data()

    def unbox_data_from_clicked_file(self):
        try:
            with open("data/"+self.path_to_file_clicked, "rb") as f:
                self.binary_data_unpacked = pickle.load(f)
                self.original_data_filepath = self.binary_data_unpacked["data_path"]
                self.original_metadata_filepath = self.binary_data_unpacked["metadata_path"]
                self.database_type = self.binary_data_unpacked["database_type"]
        except FileNotFoundError as e:
            print('File not found, error message {}'.format(e))

    def print_data(self):
        for d in self.data:
            print(d)

    def print_file_clicked(self):
        print(self.path_to_file_clicked)

    def rowCount(self, index):
        return len(self.data)

    def columnCount(self, index):
        linked_filed_length = len(
            self.file_handler.metadata[0]["linked_files"])
        return len(self.file_handler.metadata[0]["columns"])-linked_filed_length

    def column_number(self):
        linked_filed_length = len(
            self.file_handler.metadata[0]["linked_files"])
        return len(self.file_handler.metadata[0]["columns"])-linked_filed_length

    def data(self, index, role=QtCore.Qt.DisplayRole):
        student = self.get_element(index)
        if index.column() == 0 and role == QtCore.Qt.DisplayRole:
            return student.brand
        elif index.column() == 1 and role == QtCore.Qt.DisplayRole:
            return student.imei_code

    def flags(self, index):
        return super().flags(index) | QtCore.Qt.ItemIsEditable  # ili nad bitovima

    def headerData(self, section, orientation, role=QtCore.Qt.DisplayRole):
        column_count = len(self.file_handler.metadata[0]["columns"])
        for column_header_name in range(0, column_count):
            if section == column_header_name and orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
                return self.file_handler.metadata[0]["columns"][column_header_name]
