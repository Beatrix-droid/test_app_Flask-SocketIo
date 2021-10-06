import tkinter as tk
from main import *

app = tk.Tk()
app.title("")


canvas1 = tk.Canvas(app, width = 400, height = 300)
canvas1.pack()

#defining the text that will appear on the app and how it will be spaced
title_app = tk.Label(app, text="A Weather App")
API_key = tk.Label(app, text="please input your API key here")
prompt_question = tk.Label(app, text="Enter the name of the city you wish to get the weather of:")

canvas1.create_window(200, 20, window=title_app)
canvas1.create_window(200, 70, window=API_key)
canvas1.create_window(200, 150, window=prompt_question)

#prompting users for their API key
API_key = tk.Entry(app)
canvas1.create_window(200, 110, window= API_key)



#prompting users to enter the city they want to see the weather of.
city_entry = tk.Entry(app)
canvas1.create_window(200, 190, window=city_entry)


#displaying the current weather
def show_weather():
	city = city_entry.get()
	key = API_key.get()
	weather_today = tk.Label(app, text=get_current_weather(city, key))
	canvas1.create_window(200, 250, window=weather_today)


tk.Button(app, text="Submit", command=show_weather).pack()


#closing the program
quit = tk.Button(app, text="QUIT", fg="red", command=quit).pack()



app.mainloop()