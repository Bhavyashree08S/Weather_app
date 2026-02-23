"""
1. A simple Weather Application built using Python and Tkinter.
2. Fetches real-time weather data from the OpenWeather API.
3. Displays current temperature and weather conditions for a user-entered city.
4. Uses python-dotenv to securely manage the API key.
"""

import requests
import os
from dotenv import load_dotenv
import tkinter
from tkinter import messagebox,PhotoImage

load_dotenv()
def get_weather(city):
    API_key = os.getenv('API_key')
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}&units=metric"

    try:
        response=requests.get(url)
        data=response.json()
        if response.status_code==200:
            result=(
                 f"Weather in {data['name']} ,{data['sys']['country']} \n"
                 f"Temperature :{data['main']['temp']} °C\n"
                 f"Humidity :{data['main']['humidity']} %\n"
                 f"Weather : {data['weather'][0]['description']}\n"
                 f"Wind Speed:{data['wind']['speed']} m/s" 
                 ) 
            result_text.config(text=result)
            result_text.pack()

        else:
                messagebox.showerror('Error',"Soemthing went Wrong Try gain with correct city name")
    except Exception as e:
        messagebox.showerror('Error',"Soemthing went wrong")


root=tkinter.Tk()
root.geometry('1000x600')

img_path=PhotoImage(file=r"assets\img.png")
bg_img=tkinter.Label(root,image=img_path)
bg_img.place(relheight=1,relwidth=1)
root.title('Weather App')


intro=tkinter.Label(root,text=" Mausam 🌦 – Your Personal Weather Companion",font=('Times new Roman',22))
intro.pack(pady=20)
des=tkinter.Label(root,text='Hello and welcome to Mausam \n🌤Mausam delivers real-time weather updates for any city around the world 🌍.\nStay informed with accurate temperature 🌡,\n humidity 💧, wind speed 🌬, and detailed weather conditions ☁ in a clean and easy-to-use interface ✨.', font=('Times new roman',16))
des.pack(pady=20)


city=tkinter.Label(root,text='Enter the city :',font=('Times New Roman',20))
city.pack(pady=20)

city_text=tkinter.Entry(root,width=25,font=('Times New Roman',20))
city_text.pack()

submit_button=tkinter.Button(root,text='Enter',font=('Times new Roman',18) ,command=lambda:get_weather(city_text.get()))
submit_button.pack(pady=20)

result_text=tkinter.Label(root,text='',font=('Times New Roman',20))
root.mainloop()

