import js
import datetime
import asyncio
import requests

# Funktion zur Speicherung in Google Sheets
async def failsave_to_google_sheets(data):
    webhook_url = "https://script.google.com/macros/s/AKfycbxwPlfonB3FwQtbZ5sI--ZKjBtDhayZS1Glqix_K4Gvhxsp4cCFUXT-qWy34LI_MaxuFA/exec"  # Google Sheets Webhook-URL
    response = await js.fetch(webhook_url, {
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "body": js.JSON.stringify(data)
    })
    result = await response.text()
    print("Google Sheets Response:", result)

import requests

async def save_to_google_sheets(data):
    webhook_url = "https://script.google.com/macros/s/AKfycbxwPlfonB3FwQtbZ5sI--ZKjBtDhayZS1Glqix_K4Gvhxsp4cCFUXT-qWy34LI_MaxuFA/exec"  # Ersetze mit deiner Webhook-URL
    try:
        response = requests.post(webhook_url, json=data)
        if response.status_code == 200:
            print("Google Sheets Response:", response.text)
        else:
            print(f"Fehler beim Senden der Daten: {response.status_code} - {response.text}")
    except Exception as e:
        print("Fehler beim Speichern der Daten:", e)




async def on_save_button_click(event):
    experiment_data = {
        "id": "UserID123",
        "time": "testzeit",
        "data": "testdaten"
    }
    await save_to_google_sheets(experiment_data)

save_button = document.getElementById("saveButton")
add_event_listener(save_button, "click", on_save_button_click)
