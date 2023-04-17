from tkinter import *
import json
import requests

root = Tk()
root.title('Weather Forecast')

try:
    api_request = requests.get('https://data.tmd.go.th/nwpapi/v1/forecast/location/hourly')
    api = json.loads(api_request.content)
except Exception as e:
    api = 'Error...'
    
my_label = Label(root, text=api)
my_label.pack()

mainloop()
