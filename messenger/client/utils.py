import json

# function  - receive message and decode it

def get_message(client):
    message = client.recv(1024)
    if message != b'':
        if type(message) == bytes:
            message_decoded_json = message.decode('utf-8')
            response = json.loads(message_decoded_json)
            if type(response) == dict:
                return response
            else:
                raise ValueError
        else:
            raise ValueError


# function - data - dict
# encoding message and send it

def send_message(sock, message):
    if not isinstance(message, dict):
        raise TypeError
    js_message = json.dumps(message)
    encoded_message = js_message.encode('utf-8')
    sock.send(encoded_message)