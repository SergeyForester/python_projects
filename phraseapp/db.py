import pymongo

# устанавливаем соединение с сервером базы данных
con = pymongo.MongoClient()

# какую базу используем
database = con['phrase_app']

# коллекцию можно выбрать так
table = database['phrases']

def get_history():
    return [el for el in table.find()]


def add_note(phrase, data):
    if phrase:
        print(phrase, data)
        table.insert_one({"title": phrase, "data": data})
        return

    print('Rejected')