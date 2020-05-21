import datetime
import socket
import sys
import time

from PyQt5 import QtWidgets

from messenger.client import utils, login_ui, client_ui
from messenger.client.new_contact_dialog import NewContactDialog

HOST = 'localhost'  # The server's hostname or IP address
PORT = 8888  # The port used by the server


class Client:
    def __init__(self, username, password):
        # client's username
        self.username = username

        # client's password
        self.password = password

        # client's socket
        self.transport = None

        # client's contacts
        self.contacts = []

        # current chat
        self.chat = None

        self.init_connection()

        dialog = QtWidgets.QDialog()
        self.ui = client_ui.ClientUI()
        self.ui.setupUi(dialog)
        self.setupMainUI()
        dialog.show()
        app.exec_()

    def setupMainUI(self):
        # greetings
        hour = datetime.datetime.now().hour
        if 7 < hour < 12:
            greetings = 'Good Morning,'
        elif 12 < hour < 18:
            greetings = 'Good Day,'
        elif 18 < hour < 23:
            greetings = 'Good Evening,'
        else:
            greetings = 'Good Night,'

        self.ui.greetingsLabel.setText(greetings.replace(',', f', {self.username}.'))

        # list of contacts
        # get list of contacts
        utils.send_message(self.transport, {'action': 'get_contacts', 'time': time.time(), 'username': self.username})
        contacts = utils.get_message(self.transport)
        self.contacts = contacts
        print(contacts)
        for contact in contacts['response']:
            self.ui.contactsListWidget.addItem(contact['username'])

        # new contact
        self.ui.newContactBtn.clicked.connect(self.new_contact)

    def init_connection(self):
        self.transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.transport.connect((HOST, PORT))

        # login user
        login = {'action': 'login', 'time': time.time(),
                 'username': self.username, 'password': self.password}

        utils.send_message(self.transport, login)
        data = utils.get_message(self.transport)

        if data['code'] == 200:
            print('Successful login')
        elif data['code'] == 404:
            # if there is no such account, it will be created automatically
            print(data['message'])
        elif data['code'] == 403:
            print(data['message'])

        # presence request
        if data['code'] == 200 or data['code'] == 404:
            presence = {'action': 'presence', 'time': time.time(), 'username': self.username}
            utils.send_message(self.transport, presence)

            if utils.get_message(self.transport)['code'] == 200:
                pass
            else:
                self.transport.close()
                sys.exit()

    def new_contact(self):
        # get list of users
        try:
            utils.send_message(self.transport, {'action': 'get_users', 'username': self.username, 'time': time.time()})

            users = utils.get_message(self.transport)

            new_contact_d = NewContactDialog([client['user'] for client in users['response']])

            new_contact_d.exec_()
            utils.send_message(self.transport, {'action': 'create_contact', 'username': self.username,
                                                'contact': new_contact_d.current, 'time': time.time()})

            if utils.get_message(self.transport)['code'] == 200:
                print(new_contact_d.current)
                self.ui.contactsListWidget.addItem(new_contact_d.current)
        except Exception as e:
            print(e)


def main():
    client = Client(login.login, login.password)


if __name__ == '__main__':
    # client = Client(username, password)

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    login = login_ui.LoginForm()
    login.setupUi(Form)
    Form.show()
    app.exec_()
    main()

    sys.exit()
