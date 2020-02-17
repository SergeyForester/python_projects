import pymongo

# устанавливаем соединение с сервером базы данных
con = pymongo.MongoClient()

# какую базу используем
database = con['phrase_app']

# коллекцию можно выбрать так
phrases = database['phrases']


def get_history():
    return [el for el in phrases.find()]


def phrase_repetitions_increase(title):
    phrase = phrases.find({'title': title})[0]
    if phrase['repetitions'] <= 5:
        phrases.update(
            {'title': title},
            {"$set": {'repetitions': phrase['repetitions'] + 1}})
        print(phrase['repetitions'] + 1)


def add_note(phrase, data):
    if phrase:
        print(phrase, data)
        phrases.insert_one({"title": phrase, "data": data, 'repetitions': 0})
        return

    print('Rejected')


def delete_request(title):
    if title:
        phrases.remove({'title': title})
