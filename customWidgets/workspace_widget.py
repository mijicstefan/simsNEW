from PySide2.QtWidgets import QMainWindow, QApplication, QAction, QPushButton, QToolBar, QSplashScreen, QDockWidget, QFileSystemModel, QTreeView, QStatusBar, QWidget, QVBoxLayout, QTabWidget, QTableView, QTableWidget, QTableWidgetItem
from PySide2.QtGui import QKeySequence, QPixmap, QIcon
from PySide2.QtCore import Qt, QDir
import sys
from customWidgets.models.abstract_table_model import AbstractTableModel
# from data_classes.databse_file_handlers.smartphone import SmartPhone


class WorkSpaceWidget(QWidget):
    def __init__(self, parent, file_clicked):
        super().__init__(parent)
        
        self.file_clicked = file_clicked
        self.abstract_table_model = AbstractTableModel(self.file_clicked)
        # self.print_file_clicked()
        self.main_layout = QVBoxLayout()
        self.create_tab_widget()
        # self.create_table(5,5)
        # self.tab_widget.addTab(self.table_widget,QIcon("img/iconXLNK.png"), "Widget Name")


    #radi    
    def print_file_clicked(self):
        print(self.file_clicked)
    #radi
    def create_tab_widget(self):
        self.tab_widget = QTabWidget(self)
        self.tab_widget.setTabsClosable(True)

    def create_table(self, rows, columns):
        table_widget = QTableWidget(rows, columns, self)

        for i in range(rows):
            for j in range(columns):
                table_widget.setItem(i, j, QTableWidgetItem(
                    "Celija " + str(i) + str(j)))
        labels = []
        for i in range(columns):
            labels.append("Kolona" + str(i))
        table_widget.setHorizontalHeaderLabels(labels)
        self.table_widget = table_widget
        





