#!include imports in pyscript.toml
#Based on https://pyscript.com/@adec3dd4-c366-46d3-9d45-84d3b0996a43/chatgpt-demo/latest
import js
from js import fetch, JSON, console

import os
import csv
import requests
import pandas as pd
from js import Uint8Array, File, URL, document
from datetime import datetime
from pyodide.ffi.wrappers import add_event_listener 
from js import window

import pyodide_http

# Patch the Requests library so it works with Pyscript
pyodide_http.patch_all()


async def send():
    webhook_url = "https://script.google.com/macros/s/AKfycbzAasuI-ELwtJA7w8AEMG_E-P3Z9WXM2xUOkdC8OOGKOtO-FWkH8uxZjVsICOl8qKaMKA/exec"
    test_data = {"id": "12345", "answer": "Test von Pyscript"}

    try:
        response = await fetch(
            webhook_url,
            {
                "method": "POST",  # Wichtig: POST-Methode explizit setzen
                "headers": {
                    "Content-Type": "application/json"
                },
                "body": JSON.stringify(test_data)
            }
        )

        if response.ok:
            result = await response.text()
            console.log("Erfolg:", result)
        else:
            console.log(f"Fehler: {response.status} - {response.statusText}")

    except Exception as e:
        console.log("Fehler:", e)

def send2():
    webhook_url = "https://script.google.com/macros/s/AKfycbyk3ZgFIEEyksS1gPiu_Zq_l3-SEZdV2ATFbs4sV0qlfaFLDysXa09H5M61q_YA1FSdeQ/exec"
    
    test_data = {"id": "12345", "answer": "Test von Pyscript"}

    try:
        response = requests.post(
            webhook_url,
            json=test_data,
            headers={
                "Content-Type": "application/json",
                "Accept": "application/json"
            },
            allow_redirects=True  # Optional
        )
        print("Status Code:", response.status_code)
        print("Antwort:", response.text)
    except Exception as e:
        print("Fehler:", e)