import pymongo

con = pymongo.MongoClient()

database = con['currency']

users = database['users']
contacts = database['contacts']
messages = database['messages']


def get_user(user):
    return users.find_one({'user': user})


def create_user(username, password):
    users.insert_one({'user': username, 'password': password})


def create_contact(username, contact):
    contacts.insert_one({'contact': contact, 'user': username})


def create_message(user, contact, text, time):
    messages.insert_one({"sender": user, "destination": contact, "time": time, "message_text": text})


def get_messages(user, contact):
    data = []

    for el in messages.find({"sender": user, "destination": contact}):
        data.append(el)
    for el in messages.find({"sender": contact, "destination": user}):
        data.append(el)

    return sorted(data, key=lambda i: i['time'])


def get_users():
    return list(users.find({}))


def get_user_contacts(username):
    return contacts.find({'user': username})

#
# def update_data(user_id, key, value):
#     history.update(
#         {'user': user_id},
#         {"$set": {key: value}})
#
#
# def create_record(user, search_type):
#     history.insert_one(
#         {'user': user, 'search_type': search_type, 'beds': 0, 'baths': 0, 'min_price': -1, 'max_price': -1})
#
# def get_user(user):
#     print(user)
#     print(history.find_one({'user':user}))
#     return history.find_one({'user':user})
#
# def get_history():
#     return history.find({})
