from PySide2.QtWidgets import QMainWindow, QApplication, QAction, QPushButton, QToolBar, QSplashScreen, QDockWidget, QFileSystemModel, QTreeView, QStatusBar, QWidget, QVBoxLayout, QTabWidget, QTableView, QTableWidget, QTableWidgetItem
from PySide2.QtGui import QKeySequence, QPixmap, QIcon
from PySide2.QtCore import Qt, QDir
import sys



class WorkSpaceWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.main_layout = QVBoxLayout()
        self.create_tab_widget()
        self.create_table(5,5)
        self.tab_widget.addTab(self.table_widget,QIcon("img/iconXLNK.png"), "Widget Name")
        

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
        





