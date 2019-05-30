import psutil
import webbrowser

import wmi


import sys

from time import sleep, time

# from botsender import send_warning

w = wmi.WMI(namespace="root\OpenHardwareMonitor")

temperature_infos = w.Sensor()

sleep_time = 1 # секунды

traffic_monitor_period = 60 # одна минута

# traffic_monitor_threshold = 10**9 # один гигабайт в байтах
traffic_monitor_threshold = 100

temperature_threshold = 20



def do_main_program():

	"""

	опрашивает сенсоры температуры и измеряет скаченный траффик

	в случае превышения температуры отправляет предупреждение (пороги отправки берутся из характеристик сенсоров)

	в случае превышения траффика загрузки отправляет сообщение о ддос атаке (порог - один гигабайт в минуту)

	TODO: 'передавать id девайса который перегрелся'

	"""
	sleep(5)
	initial_bytes_recv = psutil.net_io_counters().bytes_recv

	initial_bytes_recv_time = time()

	for x in range(1000):
		# temps = psutil.sensors_temperatures()
		

		# for name, entries in temps.items():

		# 	for entry in entries :
			for sensor in temperature_infos:
				print('Пытаюсь зайти в иф')

				if sensor.SensorType == u'Temperature':
					print('Зашел')

					print(str(sensor.Name)  + ' ' + str(sensor.Max))

					if float(sensor.Value) >= float(temperature_threshold):

						device_name = sensor.Name

						send_warning('temperature_high', sensor.Value, name = device_name)

						if float(sensor.Value) >= float(75):

							send_warning(type_of_message='temperature_critical', measure=sensor.Value)

				if time()-initial_bytes_recv_time >= traffic_monitor_period:

					traffic_delta = psutil.net_io_counters().bytes_recv- initial_bytes_recv

					if traffic_delta >= traffic_monitor_threshold:

						send_warning(type_of_message='traffic_overload', measure=traffic_delta)

						initial_bytes_recv = psutil.net_io_counters().bytes_recv

					initial_bytes_recv_time = time()

				sleep(sleep_time)

			do_main_program()	
			sleep(5)				

# import telegram

def send_warning(type_of_message, measure,*args, **kvargs):

	"""

	отправляет сообщение пользователю от лица телеграм бота

	тип сообщения может быть предупреждением о превышении температуры цп или о превышении траффика загрузки

	дополнительно сообщает о размере превышения

	"""

	# proxy_server = telegram.utils.request.Request(proxy_url='socks5://127.0.0.1:1080/')

	# bot = telegram.Bot(token=, request=proxy_server)

	if type_of_message == 'temperature_high':

		text_of_message = 'температура устройства {} высокая и составляет {}'.format(kvargs['name'], str(measure))

		# bot.send_message(chat_id=, text=text_of_message)
		webbrowser.open(f'https://alarmerbot.ru/?key=64af56-ab4bba-456f49&message={text_of_message}')

	if type_of_message == 'temperature_critical':

		text_of_message = 'температура устройства {} критическая и составляет {}'.format(kvargs['name'], str(measure))

		# bot.send_message(chat_id=, text=text_of_message)
		webbrowser.open(f'https://alarmerbot.ru/?key=64af56-ab4bba-456f49&message={text_of_message}')
	if type_of_message == 'traffic_overload':

		text_of_message = 'устройство превысило порог загрузки и загрузило {} байт за минуту'.format(str(measure))

		# bot.send_message(chat_id=, text=text_of_message)
		webbrowser.open(f'https://alarmerbot.ru/?key=64af56-ab4bba-456f49&message={text_of_message}')

	if type_of_message == 'starting': # системное сообщение. measure можно использовать для кодов

		text_of_message = 'программа запущена'
		webbrowser.open(f'https://alarmerbot.ru/?key=64af56-ab4bba-456f49&message={text_of_message}')
	# bot.send_message(chat_id=, text=text_of_message)

import daemon


send_warning(type_of_message='starting', measure=-1)


do_main_program()

