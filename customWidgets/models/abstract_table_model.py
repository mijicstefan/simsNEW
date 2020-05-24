from PySide2 import QtWidgets
from PySide2.QtCore import QAbstractTableModel
from data_classes.databse_file_handlers.serial_file_handler import SerialFileHandler
import pickle



class AbstractTableModel(QAbstractTableModel):
    def __init__(self, file_clicked):
        super().__init__()
        self.path_to_file_clicked = file_clicked
        self.binary_data_unpacked = None
        self.unbox_data_from_clicked_file()
        self.print_unpacked_data()
        self.final_data = SerialFileHandler(self.original_data_filepath, self.original_metadata_filepath) if self.database_type == "serial" else 0
        self.print_real_data()

        #min = a if a < b else b 

    def unbox_data_from_clicked_file(self):
        try:
            with open("data/"+self.path_to_file_clicked, "rb") as f:
                self.binary_data_unpacked = pickle.load(f)
                self.original_data_filepath = self.binary_data_unpacked["data_path"]
                self.original_metadata_filepath = self.binary_data_unpacked["metadata_path"]
                self.database_type = self.binary_data_unpacked["database_type"]
        except FileNotFoundError as e:
            print('File not found, error message {}'.format(e))


    def print_real_data(self):
        print(self.final_data.get_all())


    def print_file_clicked(self):
        print(self.path_to_file_clicked)

    def print_unpacked_data(self):
        print("Data path: {}, Metadata path: {}, databaseType: {}".format(self.original_data_filepath, self.original_metadata_filepath, self.database_type))

    def row_count(self, index):
        pass  

    def columnCount(self, index):
        pass


    def data(self):
        pass
         