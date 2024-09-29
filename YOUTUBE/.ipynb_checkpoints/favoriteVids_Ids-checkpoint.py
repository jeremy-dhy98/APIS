# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 12:04:06 2024

@author: mulwa
"""

from googleapiclient.discovery import build
import os
import json
api_key = os.environ.get("YOUTUBE_API")

yt = build("youtube", version= "v3", developerKey=api_key)


def jprint(obj):
    """An helper function for better response formatting"""
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


def querry_puppies():
    """Querry favourite ids of videos of puppie from US"""
    request = yt.search().list(part="id", type="video",
                        regionCode="US", order="relevance",
                        q="puppies", maxResults=100,
                        fields="items(id(videoId))")
    response = request.execute()
    print(f"\nPuppies VideoIds: {jprint(response)}")
    return response

    
def querry_kitties():
    """Querry favourite ids of videos of kitties from US"""
    request2 = yt.search().list(part="id", type="video",
                        regionCode="US", order="relevance",
                        q="kitties", maxResults=100,
                        fields="items(id(videoId))")
    response2 = request2.execute()
    print(f"\nKitties VideoIds: {jprint(response2)}")
    return response2
    





    