import datetime

from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.html import strip_tags

import db


def findElemInListByName(list, name):
    index = 0
    for dataEl in list:
        if dataEl[1] == name:
            return index
        else:
            index += 1



def main_page(request):
    data_rooms = db.all('mainapp_room')
    data_bookings = db.all('mainapp_dateitem')
    data_images = db.all('mainapp_dataimages')
    data_ = db.all('mainapp_data')

    print(data_rooms)
    print(data_bookings)
    print(data_images)
    print(data_)



    bannerPhoto1 = data_images[findElemInListByName(data_images, 'headerPhoto1')][2]
    bannerPhoto2 = data_images[findElemInListByName(data_images, 'headerPhoto2')][2]
    bannerPhoto3 = data_images[findElemInListByName(data_images, 'headerPhoto3')][2]

    joinUs = data_[findElemInListByName(data_, 'joinUs')][2]

    advantages = data_[findElemInListByName(data_, 'advantages')][2]

    headerDescription = data_[findElemInListByName(data_, 'headerDescription')][2]

    threeWords = data_[findElemInListByName(data_ , 'threeWords')][2]

    textAfterThreeWords = data_[findElemInListByName(data_ ,'textAfterThreeWords')][2]

    nameOfHotel = data_[findElemInListByName(data_, 'nameOfHotel')][2]

    longDescriptionOfHotel = data_[findElemInListByName(data_, 'longDescription')][2]

    photoDescr1 = data_images[findElemInListByName(data_images, 'photoDescription1')][2]
    photoDescr2 = data_images[findElemInListByName(data_images, 'photoDescription2')][2]
    photoDescr3 = data_images[findElemInListByName(data_images, 'photoDescription3')][2]
    photoDescr4 = data_images[findElemInListByName(data_images, 'photoDescription4')][2]

    bookingPhoto1 = data_images[findElemInListByName(data_images, 'infoPhoto1')][2]
    bookingPhoto2 = data_images[findElemInListByName(data_images, 'infoPhoto2')][2]
    bookingPhoto3 = data_images[findElemInListByName(data_images, 'infoPhoto3')][2]

    bookAHotelRoom = data_[findElemInListByName(data_, 'bookAHotel')][2]

    stars = data_[findElemInListByName(data_, 'stars')][2]

    nameOfHotelInfo = data_[findElemInListByName(data_, 'nameOfHotelInfo')][2]

    address = data_[findElemInListByName(data_, 'address')][2]

    postalCode = data_[findElemInListByName(data_, 'postalCode')][2]

    mapCode = data_[findElemInListByName(data_, 'mapCode')][2]

    feature1 = data_[findElemInListByName(data_, 'feature1')][2]
    feature2 = data_[findElemInListByName(data_, 'feature2')][2]
    feature3 = data_[findElemInListByName(data_, 'feature3')][2]
    feature4 = data_[findElemInListByName(data_, 'feature4')][2]
    feature5 = data_[findElemInListByName(data_, 'feature5')][2]
    feature6 = data_[findElemInListByName(data_, 'feature6')][2]
    feature7 = data_[findElemInListByName(data_, 'feature7')][2]
    feature8 = data_[findElemInListByName(data_, 'feature8')][2]

    termsAndConditions = data_[findElemInListByName(data_, 'termsAndConditions')][2]

    current_day = f''

    year = datetime.datetime.today().year
    month = str(datetime.datetime.today().month) if len(str(datetime.datetime.today().month)) == 2 else f'0{datetime.datetime.today().month}'
    day = str(datetime.datetime.today().day) if len(str(datetime.datetime.today().day)) == 2 else f'0{datetime.datetime.today().day}'

    current_day = f'{year}-{month}-{day}'

    days = []
    for dayR in range(14):
        day = datetime.date.today() + datetime.timedelta(days=dayR)
        print(day)
        days.append(day)

    # roomData = {}
    # count = 0
    # for room in data_rooms:
    #     for busy in data_bookings:
    #         roomData[count] = []
    #         for day in days:
    #             if day == data_bookings[count].date_item:
    #                 if room.name == busy.room.name:
    #                     print(f'if room.name == busy.room.name  {count}')
    #                     roomData[count].append(room.name)
    #                     roomData[count].append(day)
    #                     print(roomData)
    #         count = count + 1

    content = {'days': days, 'bannerPhoto1': bannerPhoto1, 'bannerPhoto3': bannerPhoto3, 'bannerPhoto2': bannerPhoto2,
     'joinUs': joinUs,
     'advantages': advantages, 'headerDescription': headerDescription,
     'threeWords': threeWords, 'textAfterThreeWords': textAfterThreeWords,
     'nameOfHotel': nameOfHotel, 'longDescriptionOfHotel': longDescriptionOfHotel,
     'photoDescr1': photoDescr1, 'photoDescr2': photoDescr2,
     'photoDescr3': photoDescr3, 'photoDescr4': photoDescr4,
     'bookingPhoto1': bookingPhoto1, 'bookingPhoto2': bookingPhoto2,
     'bookingPhoto3': bookingPhoto3, 'bookAHotelRoom': bookAHotelRoom,
     'stars': stars, 'nameOfHotelInfo': nameOfHotelInfo,
     'address': address,
     'postalCode': postalCode, 'mapCode': mapCode,
     'feature1': feature1, 'feature2': feature2,
     'feature3': feature3, 'feature4': feature4,
     'feature5': feature5, 'feature6': feature6,
     'feature7': feature7, 'feature8': feature8,
     'termsAndConditions': termsAndConditions, 'rooms':data_rooms, 'bookings': data_bookings,
    'current_day':current_day}

    return render(request, 'mainapp/index.html', content)


def book_room(request, pk):
    print(pk)

    room = db.get_object_or_404('mainapp_room', f'id={pk}')
    days = []
    for dayR in range(14):
        day = datetime.date.today() + datetime.timedelta(days=dayR)
        print(day)
        days.append(day)
    data_ = db.all('mainapp_data')

    nameOfHotel = data_[findElemInListByName(data_, 'nameOfHotel')][2]

    if request.method == "POST":
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        email = request.POST.get('email')
        number = request.POST.get('number')
        date_from = request.POST.get('date-from')
        date_to = request.POST.get('date-to')
        print(name, surname, email, number, date_from, date_to)


        html_m = render_to_string('mainapp/assets/mail_template.html', {'nameOfHotel': nameOfHotel, 'name':name,
                                                                        'surname':surname, 'date_from':date_from,
                                                                        'date_to':date_to, 'room': room[1]})

        send_mail(f'{nameOfHotel.upper()} reservation', '' , settings.EMAIL_HOST_USER, [email], html_message=html_m, fail_silently=False)

    else:
        pass

    content = {'room': room, 'days': days,'nameOfHotel':nameOfHotel, 'bookings':db.all('mainapp_dateitem')}

    print(room)

    return render(request,'mainapp/book_room.html', content)
