import requests
import tkinter as tk
from tkinter import messagebox

# Function to fetch weather data
def fetch_weather():
    city = city_entry.get()
    api_key = "fa861ae77e724cef99c51659241411"  # Api key
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"

    try:
        response = requests.get(url)
        data = response.json()
        
        if response.status_code == 200:
            location = data['location']['name']
            temperature = data['current']['temp_c']
            condition = data['current']['condition']['text']
            weather_label.config(text=f"Location: {location}\nTemperature: {temperature}°C\nCondition: {condition}")
        else:
            messagebox.showerror("Error", data.get("error", {}).get("message", "Unable to fetch weather data"))
    except Exception as e:
        messagebox.showerror("Error", "Unable to fetch weather data")

# Set up the GUI
root = tk.Tk()
root.title("Weather App")

city_label = tk.Label(root, text="City:")
city_label.pack()
city_entry = tk.Entry(root)
city_entry.pack()

fetch_button = tk.Button(root, text="Fetch Weather", command=fetch_weather)
fetch_button.pack()

weather_label = tk.Label(root, text="")
weather_label.pack()

# Run the application
root.mainloop()