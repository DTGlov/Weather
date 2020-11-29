from tkinter import *
import requests
import json
from PIL import ImageTk,Image

root = Tk()
root.title('Clouds')
root.iconbitmap("weather.ico")
root.geometry("600x100")

# Create Zipcode Lookup Function
def zipLookup():
    # zip.get()
    # zipLabel = Label(root,text=zip.get())
    # zipLabel.grid(row=1,column=0,columnspan=2)

# Generate your own api key from airnowapi.org and replace zipcode in api key with zip.get()
    try:
        api_request = requests.get("https:insert your api key=" + zip.get() + "&distance=5&API_KEY=84AEE868-EE52-405E-87AC-3B745411767B")
        api = json.loads(api_request.content)
        city = api[0]['ReportingArea']
        quality = api[0]['AQI']
        category = api[0]['Category']['Name']

        if category == 'Good':
            weather_color = "#00e400"
        elif category == "Moderate":
            weather_color = "#ffff00"
        elif category == "Unhealthy for Sensitive Groups":
            weather_color = "#ff7e00"
        elif category == "Unhealthy":
            weather_color = "#ff0000"
        elif category == "Very Unhealthy":
            weather_color = "#8f3f97"
        elif category == "Hazardous":
            weather_color = "#7e0023"

        root.configure(background=weather_color)
        my_label = Label(root, text=city + " Air Quality " + str(quality) + " " + category, font=("Roboto", 15),
                         background=weather_color)
        my_label.grid(row=1,column=0,columnspan=2)
    except Exception as e:
        api = "Error"


zip = Entry(root)
zip.grid(row=0,column=0,stick=W+E+N+S)

zipButton = Button(root,text = "Lookup Zipcode",command= zipLookup)
zipButton.grid(row=0,column=1)
root.mainloop()