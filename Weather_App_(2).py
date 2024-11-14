import requests
import tkinter as tk
from tkinter import messagebox

# Function to fetch weather data
def fetch_weather():
    city = city_entry.get()
    api_key = "fa861ae77e724cef99c51659241411"  # Your API key
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"

    try:
        response = requests.get(url)
        data = response.json()
        
        if response.status_code == 200:
            location = data['location']['name']
            temperature = data['current']['temp_c']
            condition = data['current']['condition']['text']
            humidity = data['current']['humidity']
            wind_speed = data['current']['wind_kph']
            #icon_url = data['current']['condition']['icon']

            # Update the weather label with more details
            weather_info = (
                f"Location: {location}\n"
                f"Temperature: {temperature}°C\n"
                f"Condition: {condition}\n"
                f"Humidity: {humidity}%\n"
                f"Wind Speed: {wind_speed} kph\n"
            )
            weather_label.config(text=weather_info)
            # Update the icon
            #update_weather_icon(icon_url)
        else:
            messagebox.showerror("Error", data.get("error", {}).get("message", "Unable to fetch weather data"))
    except Exception as e:
        messagebox.showerror("Error", "Unable to fetch weather data")

def update_weather_icon(icon_url):
    # Clear previous icon if exists
    for widget in icon_frame.winfo_children():
        widget.destroy()
    
    # Load and display the weather icon
    icon_response = requests.get("http:" + icon_url)
    if icon_response.status_code == 200:
        icon_image = tk.PhotoImage(data=icon_response.content)
        icon_label = tk.Label(icon_frame, image=icon_image)
        icon_label.image = icon_image  # Keep a reference to avoid garbage collection
        icon_label.pack()

# Set up the GUI
root = tk.Tk()
root.title("Weather App")
root.geometry("300x400")  # Set a fixed size for the window

# City input
city_label = tk.Label(root, text="Enter City:", font=("Arial", 14))
city_label.pack(pady=10)
city_entry = tk.Entry(root, font=("Arial", 14))
city_entry.pack(pady=10)

# Fetch button
fetch_button = tk.Button(root, text="Fetch Weather", command=fetch_weather, font=("Arial", 14))
fetch_button.pack(pady=10)

# Weather information display
weather_label = tk.Label(root, text="", font=("Arial", 12), justify="left")
weather_label.pack(pady=10)

# Weather icon display
icon_frame = tk.Frame(root)
icon_frame.pack(pady=10)

# Run the application
root.mainloop()