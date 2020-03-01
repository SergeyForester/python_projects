import pymongo

# устанавливаем соединение с сервером базы данных
con = pymongo.MongoClient()

# какую базу используем
database = con['real_estate']

# коллекцию можно выбрать так
history = database['history']


def update_data(user_id, key, value):
    history.update(
        {'user': user_id},
        {"$set": {key: value}})


def create_record(user, search_type):
    history.insert_one(
        {'user': user, 'search_type': search_type, 'beds': 0, 'baths': 0, 'min_price': -1, 'max_price': -1})

def get_user(user):
    print(user)
    print(history.find_one({'user':user}))
    return history.find_one({'user':user})

def get_history():
    return history.find({})
