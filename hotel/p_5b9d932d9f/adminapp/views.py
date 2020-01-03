import os

from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, get_object_or_404
import datetime
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required
import platform
from django.contrib.auth.models import User

# Create your views here.
import db


def mainAdminPage(request):
    data_rooms = db.all('mainapp_room')
    data_bookings = db.all('mainapp_dateitem')

    today = datetime.date.today()

    days = []
    for dayR in range(14):
        day = datetime.date.today() + datetime.timedelta(days=dayR)
        print(day)
        days.append(day)

    context = {'roomTable': data_rooms, 'roomBusy': data_bookings, 'today': today,
               'days': days}

    return render(request, 'adminapp/index.html', context)


def is_room_name_unique(lst, value):
    # list of dictionaries
    # value - value of key
    for el in lst:
        print(el)
        if el[1] == value:
            return False
        else:
            continue

    return True


def createARoom(request):
    data_ = db.all('mainapp_room')
    # try:
    if request.method == 'POST':
        name = request.POST['name']
        price = request.POST['price']
        adults = request.POST['adults']
        kids = request.POST['kids']
        infants = request.POST['infants']
        extraPerson = request.POST['extraPerson']
        image1 = request.FILES['image1']
        image2 = request.FILES['image2']
        if request.POST['description']:
            description = request.POST['description']
        else:
            description = ''

        if not is_room_name_unique(data_, name):  # if room name is not unique
            print('inside second if')
            for number in range(2, 999999):  # trying to find number for room
                print(number)
                if is_room_name_unique(data_, name + f'{str(number)}'):  # if this number is ok
                    name += f'{str(number)}'  # set it
                    break

        fs = FileSystemStorage(location='media/rooms/')
        fs.save(image1.name, image1)
        fs.save(image2.name, image2)

        db.insert('mainapp_room',
                  [name, price, adults, kids, infants, extraPerson, image1.name, image2.name, description],
                  '(name, price, adults, kids, infants, extraPerson, image1, image2, description)')

        return HttpResponseRedirect(reverse('s-admin:main'))

    # except:
    #     raise Http404('Возникли проблемы ):')

    return render(request, 'adminapp/admin-create.html')


def viewAllRooms(request):
    rooms = db.all('mainapp_room')

    context = {'rooms': rooms}
    return render(request, 'adminapp/admin-allrooms.html', context)


def editRoom(request, pk):
    data_ = db.all('mainapp_room')
    try:
        room = db.get_object_or_404('mainapp_room', f'id={pk}')
    except:
        raise Http404('Пока-что нет такой комнаты')

    if request.method == 'POST':
        name = request.POST['name']
        price = request.POST['price']
        adults = request.POST['adults']
        kids = request.POST['kids']
        infants = request.POST['infants']
        extraPerson = request.POST['extraPerson']
        image1 = request.FILES['image1']
        image2 = request.FILES['image2']
        if request.POST['description']:
            description = request.POST['description']
        else:
            description = ''

        if not is_room_name_unique(data_, name):  # if room name is not unique
            print('inside second if')
            for number in range(2, 999999):  # trying to find number for room
                print(number)
                if is_room_name_unique(data_, name + f'{str(number)}'):  # if this number is ok
                    name += f'{str(number)}'  # set it
                    break

        fs = FileSystemStorage(location='media/rooms/')
        fs.save(image1.name, image1)
        fs.save(image2.name, image2)

        db.update('mainapp_room',
                  [{'room': room}, {'price': price}, {'adults': adults}, {'kids': kids}, {'infants': infants},
                   {'extraPerson': extraPerson}, {'image1':image1.name}, {'image2':image2.name}], f'id = {room[0]}')
        return HttpResponseRedirect(reverse('s-admin:main'))

    context = {'room': room}

    return render(request, 'adminapp/admin-roomEdit.html', context)


def bookARoom(request):
    month = {'1': 'Jan', '2': 'Feb', '3': 'Mar', '4': 'Apr', '5': 'May', '6': 'Jun', '7': 'Jul',
             '8': 'Aug', '9': 'Sep', '10': 'Oct', '11': 'Nov', '12': 'Dec'}

    room_name = request.GET['room']
    dateDay = request.GET['dateDay']
    dateMonth = request.GET['dateMonth']
    dayYear = request.GET['dateYear']

    mon = month[dateMonth]

    str = f'{mon} {dateDay} {dayYear}'
    dateTime = datetime.datetime.strptime(str, '%b %d %Y')

    room = Room.objects.get(name=room_name)

    try:
        print('try')
        DateItem.objects.get(date_item=dateTime, room=room, is_busy=True).delete()
    except:
        print('except')
        DateItem.objects.create(date_item=dateTime, room=room, is_busy=True)

    return HttpResponseRedirect(reverse('admin:main'))
