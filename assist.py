# -*- coding: utf-8 -*-


import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os

import random  #used in images
from PIL import Image # Python Imaging Library

#importing my files 
from funt import AUDIO
from funt import userinput
from funt import scommand
from funt import find_file_name
from funt import testing_model
from funt import get_category
import sys 
#import module1.image_classifier

#AUDIO("Hey shrn, How you doing?")
AUDIO("hi,how can i help you mam") #Starting Personal Voice Assistant
#hello()
 
#testing
if __name__ == "__main__":
    #tuserinput()
    while True:
    # if 1:
        query = userinput().lower()
        
        if 'stop' in query:   #stop the assistant
            AUDIO("ok!,see you soon")
            sys.exit()
        # Logic for executing tasks based on query
        elif 'how are you' in query:
            AUDIO("i am good missing sharon")
            
        elif 'what is' in query:
            AUDIO('Searching Wikipedia...')
            query = query.replace("what is", "")
            results = wikipedia.summary(query, sentences=2)
            AUDIO("According to Wikipedia")
            print(results)
            AUDIO(results)

        elif 'open youtube' in query:
            #my code shrn
            #get -> specifies registered browser
            #open --> arg1 = url, arg2 = to tell assistant to open in same-tab,new-tab,new window
            webbrowser.get("chrome").open("youtube.com", new=2) 

        elif 'open google' in query:
            webbrowser.get("chrome").open('google.com', new=2)
            #webbrowser.open("google.com", new=2)

        elif 'open stack overflow' in query:
            webbrowser.get("chrome").open("stackoverflow.com", new=2)   

        elif 'tell me the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            AUDIO(f"sharon, the time is {strTime}")
        
        elif 'open document' in query: #my code /shrn
            # speak("opening document")
            # power = r"C:\\Users\\Desktop\\word file.txt"
            # os.startfile(power)
            
            
            AUDIO("Tell me the drive name!")
            drive_name = scommand()
            AUDIO("Tell me the file name!")
            file_name = scommand().lower()
            #path = f"{drive_name}:\\"
            #find_file_name((drive_name+":"), file_name)          
            path = f"{drive_name.upper()}:\\"
            find_file_name((drive_name.upper()+":\\"), file_name)
            
        elif 'show birthday pictures' in query: #my code
            path="E:\\NEWWWWWWWWWWWWWWWWWW\\IACSD\\project work\\images\\"
            files=os.listdir(path)
            d=random.choice(files)  #chooses random image and display
            #os.startfile(d)
            #print(d)
            print(query)
            img = Image.open(path+d)
            img.show()
        
        elif "show pictures" in query:
            categories = get_category()            
            testing_model(categories)
            pass
            
        else:
            AUDIO("I'm sorry, i don't have an answer for this.")