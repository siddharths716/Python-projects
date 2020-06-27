from tkinter import *
from PIL import ImageTk , Image
root = Tk()
root.title("Weather app")
root.geometry("400x50")

#http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=6&API_KEY=75CFCD0E-CC8C-47DF-92D3-930FCDD230AF
import requests
import json



def ziplookup():
    zip.get()
    mailabel = Label(root , text = zip.get()).pack()
    try:
        api_requests = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=+"+ zip.get()+"&distance=6&API_KEY=75CFCD0E-CC8C-47DF-92D3-930FCDD230AF")
        api = json.loads(api_requests.content)
        city = api[0]["ReportingArea"]
        quality =  api[0]["AQI"]
        category = api[0]["Category"]['Name']
        mylabel = Label(root , text= city + " Air Quality " + str(quality) + " " + category , font = ("Helvectica" , 20) , background = "green")  
        mylabel.pack() 

    except Exception as e:
        api = "error...."
        
        
zip = Entry(root)
zip.pack()
    
mybutton = Button(root , text = "input the  zipcode" , command = ziplookup) 
mybutton.pack()


    
root.mainloop()