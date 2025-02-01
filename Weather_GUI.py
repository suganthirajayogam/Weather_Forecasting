from tkinter import *
import requests, json
window=Tk()
t= StringVar()
p= StringVar()
h= StringVar()
c=StringVar()
c.set("Enter City")
api_key = "c933ed56e8ebf0eef5dece823984a0c8"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
def current_temp_pressure():
    complete_url = base_url + "appid=" + api_key + "&q=" + c.get()
    print(complete_url)
    response = requests.get(complete_url)
    x = response.json()
    print("------------------")
    print("Json Data")
    print(x)
    print("----------------")
    if x["cod"] != "404":
        y = x["main"]
        z = x["weather"]
        t.set(y["temp"])
        p.set(y["pressure"] )
        h.set(y["humidity"])
    else:
        print("City not found")
Label(window,text="City Name").grid(row=0)
Label(window,text="Temparature").grid(row=1)
Label(window,text="Pressure").grid(row=2)
Label(window,text="Humadity").grid(row=3)
cityTxt=Entry(window, textvariable=c).grid(row=0,column=1)
tempTxt=Entry(window, textvariable=t).grid(row=1,column=1)
presTxt=Entry(window, textvariable=p).grid(row=2,column=1)
humTxt=Entry(window, textvariable=h).grid(row=3,column=1)
get=Button(window,text="Get",command=current_temp_pressure).grid(row=4)
mainloop()
