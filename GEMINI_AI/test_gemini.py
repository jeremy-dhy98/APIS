import os
import google.generativeai as genai

# configure gemini
api_key = os.environ.get("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

# Define model to use
model = genai.GenerativeModel("gemini-1.5-flash")

# Define prompt--> text. image, video, audio
prompt = "Why choose python over other programming languages?"
response = model.generate_content(prompt)

print(response.text) # print output as text

