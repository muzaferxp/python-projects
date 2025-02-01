import os
from mistralai import Mistral
import streamlit as st


#pip install mistralai streamlit

# Retrieve the API key from environment variables
api_key = "MISTRAL_API_KEY"

# Specify model
model = "pixtral-12b-2409"
# Initialize the Mistral client
client = Mistral(api_key=api_key)

image_url = "https://5.imimg.com/data5/PB/EA/XR/SELLER-14961972/screenshot-2-500x500.jpg"
# Define the messages for the chat
messages = [
    {
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": "Extract All the infomation in json format"
            },
            {
                "type": "image_url",
                "image_url": image_url
            }
        ]
    }
]

# Get the chat response
chat_response = client.chat.complete(
    model=model,
    messages=messages
)


st.image(image_url)
# Print the content of the response
st.markdown(chat_response.choices[0].message.content)
