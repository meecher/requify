import requests

def send():
    webhook_url = "https://script.google.com/macros/s/AKfycbxiGw0d_3QZp9uLzOLMtopQ1QVtYmJsQ1ujDZh5ZJkgcYItpXUdnYn63t8Iiwr-oTHmlg/exec"

    # Test-Daten
    test_data = {
        "id": "12345",
        "answer": "Test4"
    }
    test_safe = {}

    try:
        response = requests.post(webhook_url, json=test_data, headers={"Content-Type": "application/json"})
        #response = requests.post(webhook_url)
        #response = requests.post(webhook_url, json=test_data, headers={"Content-Type": "application/json"})

        print()
        print(f"Status Code: {response.status_code}")
        print("Antwort:", response.text)
    except Exception as e:
        print("Fehler beim Senden:", e)

def send2():
    webhook_url = "https://script.google.com/macros/s/AKfycbzAasuI-ELwtJA7w8AEMG_E-P3Z9WXM2xUOkdC8OOGKOtO-FWkH8uxZjVsICOl8qKaMKA/exec"
    
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

send2()