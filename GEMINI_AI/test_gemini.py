import os
import google.generativeai as genai

# configure gemini
api_key = os.environ.get("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

# Define model to use
model = genai.GenerativeModel("gemini-1.5-flash")

# Upload file
file_path = r"VID-20241121-WA0003.mp4"
print("Uploading file...")
def upload():
    try:
        file = genai.upload_file(file_path)
        print(f"Uploaded file: {file.name}")
        print("File uploaded sucessfully...")
    except:
        pass
    else:
         return file
    
# Define prompt--> text. image, video, audio
file = upload()
prompt = "Generate a python script which executes the sound in this video\
          when expressed in text format."
response = model.generate_content([file, "\n\n", prompt])

print(response.text) # print output as text

