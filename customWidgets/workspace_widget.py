from PySide2.QtWidgets import QMainWindow, QApplication, QAction, QPushButton, QToolBar, QSplashScreen, QDockWidget, QFileSystemModel, QTreeView, QStatusBar, QWidget, QVBoxLayout, QTabWidget, QTableView, QTableWidget, QTableWidgetItem, QAbstractItemView
from PySide2.QtGui import QKeySequence, QPixmap, QIcon
from PySide2.QtWidgets import QInputDialog, QLineEdit
from PySide2.QtCore import Qt, QDir
import sys
from customWidgets.models.abstract_table_model import AbstractTableModel
# from customWidgets.table_input_dialog import TableInputDialog
# from data_classes.databse_file_handlers.smartphone import SmartPhone


class WorkSpaceWidget(QWidget):
    def __init__(self, parent, file_clicked):
        super().__init__(parent)
        self.main_layout = QVBoxLayout()
        # Tool Bar
        self.toolbar = QToolBar(self)
        # delete action on toolbar
        self.delete_action_tb = QAction("DELETE TABLE ROW", self)
        self.delete_action_tb.setStatusTip("Obrisi Red U Tabeli")
        self.delete_action_tb.triggered.connect(self.delete_table_row_tb)
        self.toolbar.addAction(self.delete_action_tb)

        # ADD ONE TOOLBAR BUTTON
        self.add_one_action_tb = QAction("ADD TABLE ROW", self)
        self.add_one_action_tb.setStatusTip("ADD SINGLE ROW TO TABLE")
        self.add_one_action_tb.triggered.connect(self.add_table_row_handler)
        self.toolbar.addAction(self.add_one_action_tb)

        self.setLayout(self.main_layout)
        self.file_clicked = file_clicked
        self.abstract_table_model = AbstractTableModel(self.file_clicked)
        self.database_type = self.abstract_table_model.database_type
        self.create_tab_widget()
        self.check_database_type_and_run()
        self.tab_widget.addTab(self.main_table, QIcon(
            "img/iconXLNK.png"), self.file_clicked)

        self.main_layout.addWidget(self.toolbar)
        self.main_layout.addWidget(self.tab_widget)

    # TODO Srediti da funkcija bise element iz tabele klikom na dugme delete u ToolBar-u.
    def delete_table_row_tb(self):
        print("Ugraditi funkciju za brisanje reda iz tabele.")

    # TODO srediti dodavnje u tabelu.
    def add_table_row_handler(self):
        # self.table_input_dialog = TableInputDialog(
        #     self, self.abstract_table_model.file_handler.metadata[0]["columns"])
        # if self.table_input_dialog.times_called > 1:
        #     print("Input dialog already oppened.")
        # else:
        #     self.main_layout.addWidget(self.table_input_dialog)
        pass

    def check_database_type_and_run(self):
        if self.database_type == "serial" or self.database_type == "sequential":
            self.create_table()
        else:
            # TODO Obraditi izuzetak.
            pass

    def create_tab_widget(self):
        self.tab_widget = QTabWidget(self)
        self.tab_widget.setTabsClosable(True)

    def create_table(self):
        self.main_table = QTableView(self.tab_widget)
        self.main_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.main_table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.main_table.setModel(self.abstract_table_model)
        # makes responsive tabel sizes
        max_width = 1620 // self.abstract_table_model.column_number()
        for width in range(self.abstract_table_model.column_number()):
            self.main_table.setColumnWidth(width, max_width)
