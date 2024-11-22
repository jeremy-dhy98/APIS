from googleapiclient.discovery import build
import os
import json
api_key = os.environ.get("YOUTUBE_API")

yt = build("youtube", "v3", developerKey=api_key)
request = yt.channels().list(part="statistics",
                             forUsername="Tim")
results = request.execute()


def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


jprint(results)
