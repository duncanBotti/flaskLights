import unittest
import requests
import json



url1 = 'http://192.168.0.179:5000/lightApp/tasks/1'
url2 = 'http://192.168.0.179:5000/lightApp/tasks/2'
url3 = 'http://192.168.0.179:5000/lightApp/tasks/3'
url4 = 'http://192.168.0.179:5000/lightApp/tasks/4'
url5 = 'http://192.168.0.179:5000/lightApp/tasks/5'
url6 = 'http://192.168.0.179:5000/lightApp/tasks/6'
url7 = 'http://192.168.0.179:5000/lightApp/tasks/7'
url8 = 'http://192.168.0.179:5000/lightApp/tasks/8'


#turn lights on one at a time 
r = requests.get(url1)
r = requests.get(url2)
r = requests.get(url3)

#turn lights off one at a time 
r = requests.get(url4)
r = requests.get(url5)
r = requests.get(url6)

#use turn lights on/off all at once, leave in state of all on 
r = requests.get(url8)
r = requests.get(url7)

