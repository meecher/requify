from openai import OpenAI


client = OpenAI(api_key="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")




response = client.chat.completions.create(
model="gpt-4o-mini",
messages=[
  {
    "role": "user",
    "content": [
      {"type": "text", "text": "What’s in this image?"},
      {
        "type": "image_url",
        "image_url": {
          "url": "https://i.ibb.co/25TW6H6/platzhalter.png",
        },
      },
    ],
  }
],
max_tokens=300,
)

print(response.choices[0])