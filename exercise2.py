import time
timestamp =time.strftime('%H:%M:%S')
hour = int(time.strftime('%H'))
if(0 < hour <= 12):
    print("Good Morning")
elif(12 < hour <= 18):
    print("Good Afternoon")
elif(18 < hour <= 20):
    print("Good Evening")
else:
    print("Good Night")