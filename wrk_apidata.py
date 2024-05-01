from pro_catapiuse import dict
import json
import requests
import os
from pathlib import Path


def conver_to_dict():
    cat_info_dict = json.loads(dict)
    return cat_info_dict


data = conver_to_dict()
print("Data length:", len(data))
print("First data info: ", data[0]["url"])

urls = []
for item in data:
    url = item["url"]
    urls.append(url)
print(urls)

# Download the images
dwnload_folder = Path(Path.home().joinpath("Desktop", "catphotos"))
def download(url, folder):
    if not os.path.exists(folder):
        os.mkdir(folder)
    for index, url in enumerate(urls):
        try:
            response = requests.get(url, stream=True)
            if response:
                file_name = f"image_{index + 1}.jpg"  # Generating a unique file name
                save_path = folder / file_name  # Combining folder path and file name

                with open(save_path, 'wb') as file:
                    for chunk in response.iter_content(chunk_size=128):
                        file.write(chunk)

                print(f"Image {index + 1} downloaded successfully.")
            else:
                print(f"Failed to download image {index + 1}. Status code: {response.status_code}")

        except Exception as e:
            print(f"Error downloading image {index + 1}: {e}")

download(urls, dwnload_folder)
