import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtSql import QSqlDatabase, QSqlRelationalTableModel, QSqlRelationalDelegate, QSqlTableModel
from PyQt5.QtWidgets import QFileDialog

from main_window import Ui_MainWindow


class Client:
    def __init__(self):
        # init GUI
        self.table_name = None
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(MainWindow)
        MainWindow.show()

        # parameters
        self.db_path = None

        self.db = None

        # events
        self.ui.openDbPushButton.clicked.connect(self.open_database)
        self.ui.saveDbPushButton.clicked.connect(self.save_change_db)
        self.ui.addRowPushButton.clicked.connect(self.add_row)
        self.ui.deleteRowPushButton.clicked.connect(self.del_row)

        self.ui.tablesListView.itemDoubleClicked.connect(self.change_table)

        sys.exit(app.exec_())

    def open_database_dialog(self):
        try:
            self.db_path = QFileDialog.getOpenFileName(self.ui.MainWindow, "Open file", '.')[0]
            print(self.db_path)
            self.ui.path_db.setText(self.db_path)
            self.db.close()
        except Exception as e:
            pass

    def open_database(self):
        try:
            self.open_database_dialog()
            self.db = QSqlDatabase.addDatabase('QSQLITE')
            self.db.setDatabaseName(self.db_path)
            self.db.open()
            self.get_tables_name()
            self.show_table()
        except Exception as err:
            print(err)

    def get_tables_name(self):
        self.ui.tablesListView.clear()
        for table_name in self.db.tables():
            self.ui.tablesListView.addItem(table_name)

    def change_table(self, name):
        self.table_name = self.ui.tablesListView.currentItem().text()
        self.show_table()

    def show_table(self):
        self.table_model = QSqlRelationalTableModel()

        if self.table_name:
            table = self.table_name
        else:
            table = [str(self.ui.tablesListView.item(i).text()) for i in range(self.ui.tablesListView.count())][0]

        self.table_model.setTable(table)
        self.table_model.select()
        self.table_model.setEditStrategy(QSqlTableModel.OnManualSubmit)
        view = self.ui.tableViewerTableView
        view.setModel(self.table_model)
        view.setItemDelegate(QSqlRelationalDelegate(view))

    def add_row(self):
        self.table_model.insertRows(self.table_model.rowCount(), 1)

    def save_change_db(self):
        if self.table_model.submitAll():
            self.ui.statusbar.showMessage('Changes were saved')
        else:
            self.ui.statusbar.showMessage(f'{self.table_model.lastError().text()}')

    def del_row(self):
        rs = list(map(lambda x: x.row(), self.ui.tableViewerTableView.selectedIndexes()))
        print(rs)
        for i in rs:
            self.table_model.removeRows(i, 1)
        self.ui.statusbar.showMessage("Row was deleted")

client = Client()
