import pymongo

# устанавливаем соединение с сервером базы данных
con = pymongo.MongoClient()

# какую базу используем
database = con['gallery']

# коллекцию можно выбрать так
images = database['images']


def get_images():
    return [el for el in images.find()]


def add_image(title):
    if title:
        images.insert_one({"title": title})
        return

    print('FAILED TO ADD IMAGES')


def delete_request(title):
    if title:
        images.remove({'title': title})


def clear_db():
    images.remove({})

# clear_db()