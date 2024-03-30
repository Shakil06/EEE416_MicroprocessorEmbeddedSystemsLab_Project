import serial
import time
import schedule
#import urllib
from urllib.request import urlopen
 
 
def update_data(values):
    # data = urlopen('https://api.thingspeak.com/update?api_key=4PI5EIACRUJHLHMV&field'+str(i)+'='+str(n))
    param = ''
 
    for index,val in enumerate(values):
        param += '&field' + str(index+1) + '=' + str(val)
    # data = urlopen('https://api.thingspeak.com/update?api_key=4PI5EIACRUJHLHMV&field1=30&field2=20&field3=10)
    data = urlopen('https://api.thingspeak.com/update?api_key=4PI5EIACRUJHLHMV' + param)
    print(data)
 
 
def main_func():
    arduino = serial.Serial('com2', 9600)
    print('Established serial connection to Arduino')
 
    arduino_data = arduino.readline()
 
    decoded_values = str(arduino_data[0:len(arduino_data)].decode("utf-8"))
    list_values = decoded_values.split('x')
 
    update_data(list_values)
 
    # for item in list_values:
    #     list_in_floats.append(float(item))
 
    # a = list_in_floats[0]
    # b = list_in_floats[1]
    # c = list_in_floats[2]
    # d = list_in_floats[3]
    # e = list_in_floats[4]
    # f = list_in_floats[5]
 
    # update_data(1, a)
    # time.sleep(0.5)
    # update_data(2, b)
    # time.sleep(0.5)
    # update_data(3, c)
    # time.sleep(0.5)
    # update_data(4, d)
    # time.sleep(0.5)
    # update_data(5, e)
    # time.sleep(0.5)
    # update_data(6, f)
 
    print(f'Collected readings from Arduino: {list_in_floats}')
 
    arduino_data = 0
    list_in_floats.clear()
    list_values.clear()
    arduino.close()
 
 
 
list_values = []
list_in_floats = []
#list_values_1 = []
#list_in_floats_1 = []
 
print('Program started')
 
schedule.every(5).seconds.do(main_func)
 
while True:
    schedule.run_pending()
    time.sleep(1)