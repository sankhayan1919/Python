# import math
# num=float(input("enter the number:"))
# root=math.sqrt(num)
# print("root is: ",root)

# print("////////////////")
# import statistics
# def mean_mode_median(statlist):
#   return statistics.mean(statlist),statistics.mode(statlist),statistics.median(statlist)
# a,b,c=mean_mode_median([10,20,30,40,50])
# print(f" mean is {a}\n mode is {b}\n median is {c}")

# print("////////////////")
# #from shutil import copyfile
# #copyfile("C:/Users/SANU/OneDrive/Desktop/Python/Store Room.py","C:/Users/SANU/OneDrive/Desktop/Python/(0).Welcome.py")

# from datetime import datetime
# date="Oct 14 1990 1:00PM"
# date_time=datetime.strptime(date, "%b %d %Y %I:%M%p")
# print(date_time)
# print(type(date_time))

# #from dateutil import parser
# #date_time=parser.parse("Oct 14 1990 1:00PM")

# print("////////////////")
# import random,itertools
# deck=list(itertools.product(range(1,14),["Spade","Club","Heart","Diamond"]))
# random.shuffle(deck)
# print(deck)
# for i in range(5):
#     print(deck[i][0], "of", deck[i][1])

# print("////////////////")
# import requests
# response=requests.get("https://www.google.com")
# print(response.text)