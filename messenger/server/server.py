import select
import socket
import time
# from server import utils, db
from  server import utils, db


class Server:
    def __init__(self, server):
        # server socket
        self.server = server

        # list of clients
        self.clients = []

        # dict <ip:port>:<client_socket>
        self.addresses = dict()

        # dict <client_name>:<ip:port>
        self.names = dict()

        self.start()

    def start(self):
        while True:
            # waiting for connection
            try:
                client, client_address = self.server.accept()
            except OSError:
                pass
            else:
                # accepted new connection
                print(f"New connection {client_address}")
                self.clients.append(client)

            recv_data_lst = []
            send_data_lst = []
            err_lst = []

            try:
                if self.clients:
                    recv_data_lst, send_data_lst, err_lst = select.select(self.clients, self.clients, [], 0)
            except OSError as err:
                print(f'Socket Error: {err}')

            # accept messages
            if recv_data_lst:
                for client_with_message in recv_data_lst:
                    try:
                        self.process_client_message(utils.get_message(client_with_message), client_with_message)
                    except Exception as err:
                        print(f'User {client_with_message.getpeername()} disconnected from server.')
                        print(err)
                        self.clients.remove(client_with_message)

                        # addr = client_with_message.getpeername()
                        # del self.addresses[f'{addr[0]}:{addr[1]}']
                        # TODO i'dont know how to delete user from self.names

    def process_client_message(self, message, client):
        print(message)
        if 'action' in message and message['action'] == 'presence' and 'time' in message and 'username' in message:
            self.names[message['username']] = client
            utils.send_message(client, {'code': 200})

        elif 'action' in message and message['action'] == 'login' \
                and 'time' in message and 'username' in message and 'username' in message and 'password' in message:
            # try to login
            user = db.get_user(message['username'])
            if user is not None:
                if user['password'] == message['password']:
                    response = {'code': 200}
                else:
                    response = {'code': 403, 'message': 'Wrong password or username'}
            else:  # if there is no such user
                response = {'code': 404,
                            'message': f'No account with username {message["username"]}. Account was created'}
                # create account
                db.create_user(message['username'], message['password'])

            utils.send_message(client, response)

        elif 'action' in message and message['action'] == 'message' and 'to_user' in message \
                and 'time' in message and 'username' in message and 'message_text' in message:
            # redirect message to user
            response = {'action': 'message', 'time': time.time(), 'from_user': message['username'],
                        'message_text': message['message_text']}
            # send message to user
            try:
                utils.send_message(self.addresses[self.names[message['to_user']]], response)
            except Exception as err:
                print(err)

            db.create_message(message["username"], message["to_user"], message["message_text"], message["time"])

            utils.send_message(client, {'code': 200})

        elif 'action' in message and message['action'] == 'get_messages' \
                and 'time' in message and 'contact' in message and 'username' in message:
            utils.send_message(client, {
                "response": [{"sender": msg["sender"], "destination": msg["destination"], "time": msg["time"],
                              "message_text": msg["message_text"]} for msg
                             in db.get_messages(message["username"], message["contact"])]})

            print({"response": [{"sender": msg["sender"], "destination": msg["destination"], "time": msg["time"],
                              "message_text": msg["message_text"]} for msg
                             in db.get_messages(message["username"], message["contact"])]})


        elif 'action' in message and message['action'] == 'get_contacts' \
                and 'time' in message and 'username' in message:
            print(db.get_user_contacts(message['username']))
            utils.send_message(client, {'response': [{'username': contact['contact']} for contact in
                                                     db.get_user_contacts(message['username'])]})


        elif 'action' in message and message['action'] == 'create_contact' \
                and 'time' in message and 'username' in message and 'contact' in message:
            db.create_contact(message['username'], message['contact'])
            utils.send_message(client, {'code': 200})

        elif 'action' in message and message['action'] == 'get_users' \
                and 'time' in message and 'username' in message:
            print({'response': [{'user': contact['user']} for contact in db.get_users()]})
            utils.send_message(client, {'response': [{'user': contact['user']} for contact in db.get_users()]})

        else:
            utils.send_message(client, {'code': 500})
        return


if __name__ == '__main__':
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setblocking(0)
    server.bind(('localhost', 8888))
    server.listen(5)

    server = Server(server)
