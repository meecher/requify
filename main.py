#!include imports in pyscript.toml
#Based on https://pyscript.com/@adec3dd4-c366-46d3-9d45-84d3b0996a43/chatgpt-demo/latest

import js
import os
import requests
import pandas as pd
from js import Uint8Array, File, URL, document
from datetime import datetime
from pyodide.ffi.wrappers import add_event_listener 

import pyodide_http

starttime = datetime.now()
file_id = "platzhalter.png"

# Patch the Requests library so it works with Pyscript
pyodide_http.patch_all()

# CSV
#df_collect = pd.DataFrame(columns=['Group', 'Time', 'Userinput', 'Response', 'Result'], index=range(50))
#df_collect = pd.DataFrame(columns=['Role', 'Content'], index=range(50))

import os

api_key = os.environ["APIKEYAI"]
if not api_key:
    raise ValueError("API-Key fehlt. Stelle sicher, dass das Secret korrekt gesetzt ist.")

print(f"API-Key geladen: {api_key[:4]}***")  # Nur für Debugging (nicht den ganzen Key anzeigen)


OPENAI_API_KEY = api_key

url = "https://api.openai.com/v1/chat/completions"
headers = {"Content-Type": "application/json",
           "Authorization": f"Bearer {OPENAI_API_KEY}"}

messages = []
data_collect = []
print("ReqAI supporting requirements creation. ")

def send():
    userElement = js.document.getElementById('userInput')
    message = userElement.value
    userElement.value = ""
    #currentmessage = 1 #counter for appending current message to df
    #df_current = pd.DataFrame(columns=['Role', 'Content'], index=range(2))

#wadads    
    #defines role of gpt model
    if len(messages) == 0:
        messages.append({"role": "system", "content": "Requirements Engineer supporting the creation of new requirements."})
        
        data_collect.append([messages[len(data_collect)].get('role')] + [messages[len(data_collect)].get('content')] + [datetime.now() - starttime])
       
    #starts first draft of requirements
    if len(messages) == 1:
        messages.append({
        "role": "user", "content": [
        {"type": "text", "text": " Write the first draft of requirements basend on the image."},
        {
        "type": "image_url",
        "image_url": {
          "url": "https://i.ibb.co/25TW6H6/platzhalter.png",
        },
        },
        ],
        },
        )
        
        data_collect.append([messages[len(data_collect)].get('role')] + [messages[len(data_collect)].get('content')] + [datetime.now() - starttime])
        #df_collect.loc[currentmessage-1] = [messages[currentmessage-1].get('role')] + [messages[currentmessage-1].get('content')]


    print("> " + message)
    messages.append({"role": "user", "content": message})

    #version select
    #data = {"model": "gpt-3.5-turbo", "messages": messages}
    data = {"model": "gpt-4o-mini", "messages": messages}
    response = requests.post(url, headers=headers, json=data)
    
    reply = response.json()["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})
    print("\n" + reply + "\n")

    #csv appending (appends on length from list)
    data_collect.append([messages[len(data_collect)].get('role')] + [messages[len(data_collect)].get('content')] + [datetime.now() - starttime])
    data_collect.append([messages[len(data_collect)].get('role')] + [messages[len(data_collect)].get('content')] + [datetime.now() - starttime])
    print(str(data_collect))

    #dataframe try (doesnt work because of indexing -> switched to list)
    #df_current.loc[currentmessage] = [messages[currentmessage].get('role')] + [messages[currentmessage].get('content')]
    #df_current.loc[currentmessage+1] = [messages[currentmessage+1].get('role')] + [messages[currentmessage+1].get('content')]
    #combine_csv()
    #df_collect = pd.concat([df_collect, df_current])
    #currentmessage += 2

def create_csv():
    ### old create csv; downloadFile new one
    #df_collect.to_csv('data.csv', index=False)
    #print(data_collect)

    #convert to df
    df_collect = pd.DataFrame(data_collect)
    df_collect.to_csv('datatest.csv', index=False)

    cwd = os.getcwd()  # Get the current working directory (cwd)
    files = os.listdir(cwd)  # Get all the files in that directory
    print("Files in %r: %s" % (cwd, files))

    #to csv
    df = pd.read_csv("datatest.csv")
    #print(df)

    file = File.new([df], "unused_file_name.txt", {type: "text/plain"})
    url = URL.createObjectURL(file)
    #df.loc[0] = df_collect
    #df.to_csv("data.csv", index=False)
    #wie csv wieder kriegen``???

def downloadFile(*args):
    #encoded_data = data.encode('utf-8')
    #my_stream = io.BytesIO(encoded_data)

    #js_array = Uint8Array.new(len(encoded_data))
    #js_array.assign(my_stream.getbuffer())
    #convert to df
    #print(str(data_collect))
    #print(str("1 " + data_collect[0]) + "2 " + str(data_collect [1]))
    #df_collect = pd.DataFrame(data_collect)
    #df_collect.to_csv('datatest.csv', index=False, header=True)

    #read csv
    #df = pd.read_csv("datatest.csv")
    #print(df)


    #create file to download

    #python lösung cant access file
    #f = open("myfile.csv", "a")
    #with open("myfile.csv", 'w', newline='') as myfile:
    #    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    #    wr.writerow(data_collect)

    #convert to str for csv
    outputAsString = ""
    for i in data_collect:
        outputAsString += str(i[0]) + ", " + str(i[1]) + ", " + str(i[2])+ "\n"

    file = File.new([outputAsString], "data.csv", {type: "text/csv"})
    url = URL.createObjectURL(file)

    hidden_link = document.createElement("a")
    hidden_link.setAttribute("download", "data.csv")
    hidden_link.setAttribute("href", url)
    hidden_link.click()

    #see files
    #cwd = os.getcwd()  # Get the current working directory (cwd)
    #files = os.listdir(cwd)  # Get all the files in that directory
    #print("Files in %r: %s" % (cwd, files))

#auto download without function
#add_event_listener(document.getElementById("download"), "click", downloadFile)

#Starts Chatbot with first draft of requirements and sets role of system
send()
