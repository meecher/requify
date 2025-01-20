import js
import datetime

async def save_to_google_sheets(user_id, answer):
    data = {
        "id": user_id,
        "answer": answer,
        "timestamp": str(datetime.datetime.now())
    }
    response = await js.fetch("https://script.google.com/macros/s/AKfycbzJ6aDt7bH-burX90ScE1j_mbESXpHvEPbWUfs63JtQ9npkj-VCLDQLkAzJWdtJ1gSBYA/exec", {
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "body": js.JSON.stringify(data)
    })
    result = await response.text()
    print(result)

# Beispielaufruf:
async def gostart():
    await save_to_google_sheets("12345", "Antwort auf Experiment")
