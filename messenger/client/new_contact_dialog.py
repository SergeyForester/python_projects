from PyQt5.QtWidgets import QDialog, QDialogButtonBox, QVBoxLayout, QComboBox, QPushButton


class NewContactDialog(QDialog):
    def __init__(self, users):
        super().__init__()

        self.setWindowTitle("New Contact")

        self.users = QComboBox()
        self.users.addItems(users)
        self.users.currentTextChanged.connect(self.userSelected)

        self.current = [self.users.itemText(i) for i in range(self.users.count())][0]

        self.addBtn = QPushButton()
        self.addBtn.setText('Add')
        self.addBtn.clicked.connect(self.addContact)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.users)
        self.layout.addWidget(self.addBtn)
        self.setLayout(self.layout)

    def addContact(self):
        self.close()

    def userSelected(self, value):
        self.current = value
