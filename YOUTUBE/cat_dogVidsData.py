# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 16:37:29 2024

@author: mulwa
"""

from favoriteVids_Ids import yt
from Vidz_Ids import response, response2


# Store cats videos data in a dict
cats_info = {
    "id": [], "views": [],
    "duration": [], "likes": [],
    "dislikes": [], "comments": [],
    "favorites": []}

# Store dogs videos data in a dict
dogs_info = {
    "id": [], "views": [],
    "duration": [], "likes": [],
    "dislikes": [], "comments": [],
    "favorites": []}

def retrieveCatVidInfo():
    for item in response["items"]:
        vidId = item["id"]["videoId"]
        # Request stats for this spacific video
        r = yt.videos().list(part="statistics, contentDetails", id=vidId,
            fields="items(statistics, contentDetails(duration))").execute()
        try:
            # Access a vids details and append them accordingly
            views = r["items"][0]["statistics"].get("viewCount", "None_key")
            duration = r["items"][0]["contentDetails"].get("duration", "None_key")
            likes = r["items"][0]["statistics"].get("likeCount", "None_key")
            dislikes = r["items"][0]["statistics"].get("dislikeCount", "None_key") 
            comments = r["items"][0]["statistics"].get("commentCount", "None_key")
            favorites = r["items"][0]["statistics"].get("favoriteCount", "None_key")
            cats_info["id"].append(vidId)
            cats_info["views"].append(views)
            cats_info["duration"].append(duration)
            cats_info["dislikes"].append(dislikes)
            cats_info["likes"].append(likes)
            cats_info["comments"].append(comments)
            cats_info["favorites"].append(favorites)
        except:
            pass
        
retrieveCatVidInfo()


def retrieveDogVidInfo():
    for item in response2["items"]:
        vidId = item["id"]["videoId"]
        # Request stats for this spacific video
        r = yt.videos().list(part="statistics, contentDetails", id=vidId,
            fields="items(statistics, contentDetails(duration))").execute()
        try:
            # Access a vids details and append them accordingly
            views = r["items"][0]["statistics"].get("viewCount", "None_key")
            duration = r["items"][0]["contentDetails"].get("duration", "None_key")
            likes = r["items"][0]["statistics"].get("likeCount", "None_key")
            dislikes = r["items"][0]["statistics"].get("dislikeCount", "None_key") 
            comments = r["items"][0]["statistics"].get("commentCount", "None_key")
            favorites = r["items"][0]["statistics"].get("favoriteCount", "None_key")
            dogs_info["id"].append(vidId)
            dogs_info["views"].append(views)
            dogs_info["duration"].append(duration)
            dogs_info["dislikes"].append(dislikes)
            dogs_info["likes"].append(likes)
            dogs_info["comments"].append(comments)
            dogs_info["favorites"].append(favorites)
        except:
            pass
        
retrieveDogVidInfo()

        