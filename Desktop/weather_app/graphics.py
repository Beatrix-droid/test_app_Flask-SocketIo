import tkinter as tk
from main import *

app = tk.Tk()
app.title("")


canvas1 = tk.Canvas(app, width = 400, height = 300)
canvas1.pack()

title_app = tk.Label(app, text="A Weather App")
prompt_question = tk.Label(app, text="Enter the name of the city you wish to get the weather of:")

canvas1.create_window(200, 70, window=title_app)

canvas1.create_window(200, 100, window=prompt_question)


city_entry = tk.Entry(app)
canvas1.create_window(200, 140, window=city_entry)

def show_weather():
	city = city_entry.get()
	weather_today = tk.Label(app, text=get_current_weather(city, current_weather_key))
	canvas1.create_window(200, 230, window=weather_today)

def show_forecast():
	city = city_entry.get()
	future_weather = tk.Label(app, text=get_forecast(city, forecast_weather_key))
	canvas1.create_window(200, 230, window=future_weather)




tk.Button(app, text="Search Current Weather", command=show_weather).pack()
tk.Button(app, text="Search Weather Forecast", command=show_weather).pack()

quit = tk.Button(app, text="QUIT", fg="red", command=quit).pack()



app.mainloop()