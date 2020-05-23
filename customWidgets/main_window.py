from PySide2.QtWidgets import QMainWindow, QApplication, QAction, QPushButton, QToolBar, QSplashScreen, QDockWidget, QFileSystemModel, QTreeView, QStatusBar
from PySide2.QtGui import QKeySequence, QPixmap, QIcon
from PySide2.QtCore import Qt, QDir
import sys

from customWidgets.workspace_widget import WorkSpaceWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        #SET => App Icon
        self.icon = QIcon("img/iconXLNK.png")
        #End

        #SET => Window Icon
        self.setWindowIcon(self.icon)
        #End

        #WSET => Window Title
        self.setWindowTitle("XLNK | Data Manager")
        #End

        #Menus
        self.menu = self.menuBar()
        self.file_menu = self.menu.addMenu("&File")
        self.edit_menu = self.menu.addMenu("&Edit")
        self.view_menu = self.menu.addMenu("&View")
        self.help_menu = self.menu.addMenu("&Help")
        #End

        #===================
        #Menu Button Actions
        
        #Exit QAction
        exit_action = QAction("Exit",self)
        exit_action.setShortcut(QKeySequence.Quit)
        exit_action.triggered.connect(self.close)
        self.file_menu.addAction(exit_action)
        #End
        #End

        #Tool Bar
        toolbar = QToolBar(self)
        self.addToolBar(toolbar)

        #delete action on toolbar
        delete_action_tb = QAction("DELETE TABLE ROW", self)
        delete_action_tb.setStatusTip("Obrisi Red U Tabeli")
        delete_action_tb.triggered.connect(self.delete_table_row_tb)
        toolbar.addAction(delete_action_tb)

        #Dock Widget
        dock_widget = QDockWidget("EXPLORER", self)
        #File System Model
        file_system_model = QFileSystemModel()
        file_system_model.setRootPath(QDir.currentPath())
        #SET => Tree View MOdel
        tree_view = QTreeView()
        tree_view.setModel(file_system_model)
        tree_view.setRootIndex(
            file_system_model.index(QDir.currentPath()))
        tree_view.clicked.connect(self.file_clicked_handler)  
        dock_widget.setWidget(tree_view)
        dock_widget.setFloating(False)

        
        self.addDockWidget(Qt.LeftDockWidgetArea, dock_widget)
        
        self.showMaximized()

    #ToolBar Functions
    #TODO
    def delete_table_row_tb(self):
        print("Ugraditi funkciju za brisanje reda iz tabele.")

    def file_clicked_handler(self):
        self.status_bar = QStatusBar(self)
        self.status_bar.showMessage("Some file is clicked", 3000)
        self.setStatusBar(self.status_bar)
        #Central Widget
        workspace_widget = WorkSpaceWidget(self)
        self.setCentralWidget(workspace_widget)

